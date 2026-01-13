import re
from collections.abc import Callable
from functools import reduce

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode


def extract_markdown_images(text: str) -> list[tuple]:
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str) -> list[tuple]:
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def _split_single_node_alternating(
    node: TextNode, delimiter: str, text_type: TextType
) -> list[TextNode]:
    """Split a single node by delimiter using alternating logic."""
    if node.text_type != TextType.TEXT:
        return [node]

    sections = node.text.split(delimiter)
    if len(sections) % 2 == 0:
        raise ValueError("Invalid markdown: delimiter not closed")

    return [
        TextNode(sections[i], text_type if i % 2 == 1 else TextType.TEXT)
        for i in range(len(sections))
        if sections[i]
    ]


def _split_single_node_markdown(
    node: TextNode,
    extract_fn: Callable[[str], list[tuple]],
    text_type: TextType,
    format_fn: Callable[[tuple], str],
) -> list[TextNode]:
    """Split a single node by markdown patterns (images/links)."""
    if node.text_type != TextType.TEXT:
        return [node]

    extracted = extract_fn(node.text)
    if not extracted:
        return [node]

    result = []
    remaining_text = node.text

    for item in extracted:
        markdown_syntax = format_fn(item)
        sections = remaining_text.split(markdown_syntax, maxsplit=1)

        if len(sections) != 2:
            raise ValueError("Invalid markdown: pattern not closed")

        if sections[0]:
            result.append(TextNode(sections[0], TextType.TEXT))

        result.append(TextNode(item[0], text_type, item[1]))
        remaining_text = sections[1]

    if remaining_text:
        result.append(TextNode(remaining_text, TextType.TEXT))

    return result


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    """
    Split nodes by delimiter (e.g., **, *, `).
    Uses alternating logic: odd indices become text_type, even become TEXT.
    """
    return [
        split_node
        for node in old_nodes
        for split_node in _split_single_node_alternating(node, delimiter, text_type)
    ]


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """Split nodes by markdown image syntax: ![alt](url)"""
    return [
        split_node
        for node in old_nodes
        for split_node in _split_single_node_markdown(
            node,
            extract_markdown_images,
            TextType.IMAGE,
            lambda img: f"![{img[0]}]({img[1]})",
        )
    ]


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """Split nodes by markdown link syntax: [text](url)"""
    return [
        split_node
        for node in old_nodes
        for split_node in _split_single_node_markdown(
            node,
            extract_markdown_links,
            TextType.LINK,
            lambda link: f"[{link[0]}]({link[1]})",
        )
    ]


def text_to_textnodes(text) -> list[TextNode]:
    transformations = [
        split_nodes_image,
        split_nodes_link,
        lambda nodes: split_nodes_delimiter(nodes, "**", TextType.BOLD),
        lambda nodes: split_nodes_delimiter(nodes, "_", TextType.ITALIC),
        lambda nodes: split_nodes_delimiter(nodes, "`", TextType.CODE),
    ]

    return reduce(
        lambda nodes, transform: transform(nodes),
        transformations,
        [TextNode(text, TextType.TEXT)],
    )


def text_to_children(text: str) -> list[HTMLNode]:
    children = []
    for text_node in text_to_textnodes(text):
        children.append(text_node_to_html_node(text_node))
    return children

from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_children
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Split markdown text into blocks separated by blank lines.
    Strips whitespace from each block and filters out empty blocks.
    """
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]


def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.CODE

    lines = block.split("\n")
    if all(line.startswith(">") or not line.strip() for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH


def _heading_to_html(block: str) -> HTMLNode:
    header, content = block.split(" ", maxsplit=1)
    return ParentNode(tag=f"h{len(header)}", children=text_to_children(content))


def _code_to_html(block: str) -> HTMLNode:
    return ParentNode(tag="pre", children=[LeafNode(tag="code", value=block[4:-4])])


def _quote_to_html(block: str) -> HTMLNode:
    processed_lines: list[str] = []
    for line in block.split("\n"):
        if line.startswith(">"):
            processed_lines.append(line[1:].lstrip(" "))
        else:
            processed_lines.append(line)

    content = "\n".join(processed_lines)
    return ParentNode(tag="blockquote", children=text_to_children(content))


def _unordered_list_to_html(block: str) -> HTMLNode:
    items = [line[2:] for line in block.split("\n")]
    return ParentNode(
        tag="ul",
        children=[
            ParentNode(tag="li", children=text_to_children(item)) for item in items
        ],
    )


def _ordered_list_to_html(block: str) -> HTMLNode:
    items = [line[3:] for line in block.split("\n")]
    return ParentNode(
        tag="ol",
        children=[
            ParentNode(tag="li", children=text_to_children(item)) for item in items
        ],
    )


def _paragraph_to_html(block: str) -> HTMLNode:
    return ParentNode(tag="p", children=text_to_children(block.replace("\n", " ")))


BLOCK_CONVERTER = {
    BlockType.HEADING: _heading_to_html,
    BlockType.CODE: _code_to_html,
    BlockType.QUOTE: _quote_to_html,
    BlockType.UNORDERED_LIST: _unordered_list_to_html,
    BlockType.ORDERED_LIST: _ordered_list_to_html,
    BlockType.PARAGRAPH: _paragraph_to_html,
}


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = [BLOCK_CONVERTER[block_to_block_type(block)](block) for block in blocks]

    return ParentNode(tag="div", children=nodes)

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
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                header, content = block.split(" ", maxsplit=1)
                nodes.append(
                    ParentNode(
                        tag=f"h{len(header)}", children=text_to_children(content)
                    )
                )
            case BlockType.CODE:
                nodes.append(
                    ParentNode(
                        tag="pre", children=[LeafNode(tag="code", value=block[4:-4])]
                    )
                )
            case BlockType.QUOTE:
                content = "\n".join([line[2:] for line in block.split("\n")])
                nodes.append(
                    ParentNode(
                        tag="blockquote",
                        children=text_to_children(content),
                    )
                )
            case BlockType.UNORDERED_LIST:
                items = [line[2:] for line in block.split("\n")]
                nodes.append(
                    ParentNode(
                        tag="ul",
                        children=[
                            ParentNode(tag="li", children=text_to_children(item))
                            for item in items
                        ],
                    )
                )
            case BlockType.ORDERED_LIST:
                items = [line[3:] for line in block.split("\n")]
                nodes.append(
                    ParentNode(
                        tag="ol",
                        children=[
                            ParentNode(tag="li", children=text_to_children(item))
                            for item in items
                        ],
                    )
                )
            case _:
                nodes.append(
                    ParentNode(
                        tag="p", children=text_to_children(block.replace("\n", " "))
                    )
                )

    return ParentNode(tag="div", children=nodes)

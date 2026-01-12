from enum import Enum
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

    if all(re.match(r"^[-]\s", line) for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(rf"^{i}\.\s", line) for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH

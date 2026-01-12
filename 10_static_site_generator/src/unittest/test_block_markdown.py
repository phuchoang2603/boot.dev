import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_multiple_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(
            result,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )

    def test_blocks_with_whitespace(self):
        markdown = """  Block with spaces  

    Another block    """
        result = markdown_to_blocks(markdown)
        self.assertEqual(
            result,
            ["Block with spaces", "Another block"],
        )

    def test_multiple_newlines_between_blocks(self):
        markdown = """Block one


Block two



Block three"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, ["Block one", "Block two", "Block three"])


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_type(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_with_multiple_hashes(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block_type(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block_type(self):
        block = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_type(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a paragraph\nwith multiple lines\nthat is not a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

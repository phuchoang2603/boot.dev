import unittest

from block_markdown import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


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


class TestBlockToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_headings_multiple_levels(self):
        md = """# Heading 1

## Heading 2

### Heading 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_code_block(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_quote_block(self):
        md = """> This is a quote
> with multiple lines
> of text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\nwith multiple lines\nof text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """- Item 1
- Item 2
- Item 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """1. First item
2. Second item
3. Third item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_unordered_list_with_inline_markdown(self):
        md = """- **Bold** item
- _Italic_ item
- `Code` item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><b>Bold</b> item</li><li><i>Italic</i> item</li><li><code>Code</code> item</li></ul></div>",
        )

    def test_heading_with_inline_markdown(self):
        md = "## This is a **bold** heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>This is a <b>bold</b> heading</h2></div>")

    def test_complex_document(self):
        md = """# Main Title

This is a paragraph with **bold** and _italic_ text.

## Section

- First item
- Second item

1. Ordered first
2. Ordered second"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Main Title</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Section</h2><ul><li>First item</li><li>Second item</li></ul><ol><li>Ordered first</li><li>Ordered second</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()

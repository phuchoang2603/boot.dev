import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none_vs_url(self):
        node = TextNode("Text", TextType.TEXT, None)
        node2 = TextNode("Text", TextType.TEXT, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("Text", TextType.TEXT, None)
        node2 = TextNode("Text", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        expected = "TextNode(This is a text node, bold, https://example.com"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()

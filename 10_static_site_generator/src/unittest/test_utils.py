import unittest

from utils import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello World\n"), "Hello World")

    def test_title_with_content(self):
        markdown = "# My Title\n\nSome content\n## Subheading"
        self.assertEqual(extract_title(markdown), "My Title")

    def test_title_with_special_chars(self):
        self.assertEqual(
            extract_title("# Welcome to *My* **Blog**!\n"), "Welcome to *My* **Blog**!"
        )

    def test_title_with_numbers(self):
        self.assertEqual(
            extract_title("# Chapter 1: The Beginning\n"), "Chapter 1: The Beginning"
        )

    def test_no_h1_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            extract_title("## This is h2\n\nNo h1 here.")
        self.assertIn("title not found", str(ctx.exception))

    def test_empty_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            extract_title("")
        self.assertIn("title not found", str(ctx.exception))

    def test_h1_not_at_start_raises_exception(self):
        # h1 must be at the very beginning of the document
        with self.assertRaises(Exception) as ctx:
            extract_title("Some text\n# The Title\n")
        self.assertIn("title not found", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()

import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        old1 = TextNode("This is text with `code` text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1], "`", TextType.CODE),
            [TextNode("This is text with ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)]
            )

    def test_asterisk(self):
        old1 = TextNode("This is text with **bold** text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1], "**", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)]
            )
        
    def test_starting_asterisk(self):
        old1 = TextNode("**This is **text with bold text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1], "**", TextType.BOLD),
            [TextNode("This is ", TextType.BOLD), TextNode("text with bold text", TextType.TEXT)]
            )

    def test_ending_asterisk(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1], "**", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold text", TextType.BOLD)]
            )
        
    def test_invalid_delimiters(self):
        old1 = TextNode("This is text with **bold text", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [old1], "**", TextType.BOLD)

    def test_double_delimiters(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1], "*", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold text", TextType.TEXT)]
        )

    def test_multiple_nodes(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        old2 = TextNode("**This is **text with bold text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1, old2], "**", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode("This is ", TextType.BOLD), TextNode("text with bold text", TextType.TEXT)]
            )
        
    def test_text_and_del(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        old2 = TextNode("This is text with bold text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([old1, old2], "**", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode("This is text with bold text", TextType.TEXT)]
            )
        
    def test_multiple_with_invalid(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        old2 = TextNode("This is text with **bold text", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [old1, old2], "**", TextType.BOLD)

    def test_mixed_types(self):
        old1 = TextNode("This is text with **bold text**", TextType.TEXT)
        old2 = TextNode("This is code text", TextType.CODE)
        self.assertEqual(
            split_nodes_delimiter([old1, old2], "**", TextType.BOLD),
            [TextNode("This is text with ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode("This is code text", TextType.CODE)]
            )

if __name__ == "__main__":
    unittest.main()
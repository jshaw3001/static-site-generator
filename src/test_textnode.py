import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_same_text_diff_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_same_type_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_all_diff(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-small.webp")
        self.assertNotEqual(node, node2)

    def test_empty_same(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_empty_diff(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_same_link_diff_other(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is also a link node", TextType.LINK, "https://www.boot.dev/dashboard")
        self.assertNotEqual(node, node2)
    
    def test_diff_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/courses")
        self.assertNotEqual(node, node2)

    

if __name__ == "__main__":
    unittest.main()
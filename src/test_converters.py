import unittest

from converters import text_node_to_html_node, markdown_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")
    
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")
    
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">This is a text node</a>')
    
    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com" alt="This is a text node"></img>')

    def test_unhandled_type(self):
        node = TextNode("This is a text node", type="div")
        self.assertRaises(Exception, text_node_to_html_node, node)

    def test_empty_text(self):
        node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b></b>")
    
    def test_none_text(self):
        node = TextNode(None, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertRaises(ValueError, html_node.to_html)

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
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

    def test_codeblock(self):
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
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
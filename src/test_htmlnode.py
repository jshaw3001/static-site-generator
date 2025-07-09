import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        node.props_to_html()

    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://example.com"})
        node.props_to_html()

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        node.props_to_html()

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev Back End Developer Course", {"href":"https://www.boot.dev/"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev/">Boot.dev Back End Developer Course</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode("a", "child2", {"href":"https://example.com"})
        parent_node = ParentNode("h1", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<h1><b>child1</b><a href="https://example.com">child2</a></h1>',
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)
        
    def test_to_html_empty_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>"
        )

if __name__ == "__main__":
    unittest.main()
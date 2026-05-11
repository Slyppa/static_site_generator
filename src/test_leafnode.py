import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        expected = "LeafNode(p, Hello, world!, None)"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_repr_with_props(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        expected = "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode(tag= 'p', value= 'algum texto', props= {'href':'https://www.google.com', 'target': '_blank',})
        expected = "HTMLNode(p, algum texto, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)
    def test_props(self):
        node = HTMLNode(tag= 'p', value= 'algum texto', props= {'href':'https://www.google.com', 'target': '_blank',})
        expected = " href='https://www.google.com' target='_blank'"
        self.assertEqual(node.props_to_html(), expected)
    
    def test_children(self):
        node1 = HTMLNode(tag= 'p', value= 'algum texto', props= {'href':'https://www.google.com', 'target': '_blank',})
        node2 = HTMLNode(tag= 'p', value= 'algum texto', props= {'href':'https://www.google.com', 'target': '_blank',})
        node_parent = HTMLNode(children= [node1, node2])
        self.assertIsNotNone(node_parent.children)
    
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
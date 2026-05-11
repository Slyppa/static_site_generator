import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    # HTMLNode
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

    # LeafNode tests    
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

    # ParentNode tests
    def test_has_tag(self):
        parent_node = ParentNode(tag= None, children=HTMLNode)
        self.assertRaises(ValueError)
    def test_has_children(self):
        parent_node = ParentNode(tag='div', children= None)
        self.assertRaises(ValueError)

    def test_to_html_with_children(self):
        child_node = LeafNode('span', 'child')
        parent_node = ParentNode('div', [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode('b', 'grandchild')
        child_node = ParentNode('span', [grandchild_node])
        parent_node = ParentNode('div', [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild</b></span></div>',
        )


if __name__ == "__main__":
    unittest.main()
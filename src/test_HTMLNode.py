import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode(tag= 'p', value= 'algum texto', props= {"href":"https://www.google.com", "target": "_blank",})
        expected = "HTMLNode(p, algum texto, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)
    def test_props(self):
        node = HTMLNode(tag= 'p', value= 'algum texto', props= {"href":"https://www.google.com", "target": "_blank",})
        expected = " href='https://www.google.com' target='_blank'"
        self.assertEqual(node.props_to_htmml(), expected)
    
    def test_children(self):
        node1 = HTMLNode(tag= 'p', value= 'algum texto', props= {"href":"https://www.google.com", "target": "_blank",})
        node2 = HTMLNode(tag= 'p', value= 'algum texto', props= {"href":"https://www.google.com", "target": "_blank",})
        node_parent = HTMLNode(children= [node1, node2])
        self.assertIsNotNone(node_parent.children)

    def valid_node(self):
        node = HTMLNode()
        self.assertRaises(Exception)

if __name__ == "__main__":
    unittest.main()
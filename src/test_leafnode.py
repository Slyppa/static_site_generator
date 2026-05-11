import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
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
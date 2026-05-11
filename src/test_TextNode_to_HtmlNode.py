import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is a text node')

    def test_bold(self):
        node = TextNode('bold text', TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'bold text')

    def test_italic(self):
        node = TextNode('italic text', TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'italic text')

    def test_code(self):
        node = TextNode('print("hi")', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'print("hi")')

    def test_link(self):
        node = TextNode('Boot.dev', TextType.LINK, 'https://www.boot.dev')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'Boot.dev')
        self.assertEqual(html_node.props, {'href': 'https://www.boot.dev'})

    def test_image(self):
        node = TextNode('A bear', TextType.IMAGE, 'https://example.com/bear.png')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(
            html_node.props,
            {'src': 'https://example.com/bear.png', 'alt': 'A bear'},
        )

    def test_invalid_type(self):
        node = TextNode('oops', 'not_a_type')
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
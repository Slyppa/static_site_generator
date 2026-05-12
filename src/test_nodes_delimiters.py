import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from Inline import split_nodes_delimiter

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode('This is text with a `code block` word', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode('This is text with a ', TextType.TEXT),
                TextNode('code block', TextType.CODE),
                TextNode(' word', TextType.TEXT),
            ],
        )

    def test_multiple_bold(self):
        node = TextNode('A **bold** and another **bold** word', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Expect 5 nodes: text, bold, text, bold, text
        self.assertTrue(
            new_nodes[0].text_type == TextType.TEXT and
            new_nodes[1].text_type == TextType.BOLD and
            new_nodes[2].text_type == TextType.TEXT and
            new_nodes[3].text_type == TextType.BOLD and
            new_nodes[4].text_type == TextType.TEXT
        )
    
    def test_delimiter_start(self):
        node = TextNode('**bold** at the start', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode('bold', TextType.BOLD),
                TextNode(' at the start', TextType.TEXT)
            ]
        )
    
    def test_delimiter_end(self):
        node = TextNode('ends with **bold**', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode('ends with ', TextType.TEXT),
                TextNode('bold', TextType.BOLD)
            ]
        )

    def test_no_delimiter(self):
        node = TextNode('plain text', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(new_nodes, [TextNode('plain text', TextType.TEXT)])
    
    def test_non_text_passthrough(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("already bold", TextType.BOLD)])

    def test_multiple_input_nodes(self):
        nodes = [
            TextNode("a `code` b", TextType.TEXT),
            TextNode("c `code` d", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        # Expect 6 nodes total
        self.assertEqual(
            new_nodes,
            [
                TextNode("a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" b", TextType.TEXT),
                TextNode("c ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" d", TextType.TEXT),
            ],
        )
    
    def test_unmatched_delimiter(self):
        node = TextNode("this is `broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
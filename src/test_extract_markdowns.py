import unittest
from Inline import extract_markdown_images, extract_markdown_links

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![first](https://a.com/1.png) text ![second](https://a.com/2.jpg)"
        )
        self.assertListEqual(
            [
                ("first", "https://a.com/1.png"),
                ("second", "https://a.com/2.jpg"),
            ],
            matches,
        )
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev")
            ],
            matches
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches
        )

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("just plain text")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links("no links here")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "![img](https://a.com/img.png) and [site](https://a.com)"
        )
        self.assertListEqual(
            [("site", "https://a.com")],
            matches,
        )

    def test_extract_markdown_links_empty_text(self):
        matches = extract_markdown_links("[](https://boot.dev)")
        self.assertListEqual([("", "https://boot.dev")], matches)


if __name__ == "__main__":
    unittest.main()
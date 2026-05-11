from textnode import TextNode, TextType

def main():
    dummy_test = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

    print(repr(dummy_test))

main()
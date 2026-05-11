from textnode import TextNode

def main():
    dummy_test = TextNode('This is some anchor text', 'link', 'https://www.boot.dev')

    print(repr(dummy_test))

main()
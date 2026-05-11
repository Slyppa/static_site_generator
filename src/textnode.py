from enum import Enum

class TextType(Enum):
    Plain = 'plain'
    Bold = 'bold'
    Italic = 'italic'
    Code = 'code'
    Link = 'link'
    Image = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url
        if text_type in TextType:
            self.text_type = text_type
        else: raise Exception('invalid type')

    def __eq__(self, other):
        return self == other
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
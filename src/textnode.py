from enum import Enum

class TextType(Enum):
    Plain = 'text'
    Bold = '**Bold text**'
    Italic = '_Italic text_'
    Code = '`Code text`'
    Link = '[anchor text](url)'
    Image = '![alt text](url)'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self == other
    
    def __repr__(self):
        return f'TextNode({self.text!r}, {self.text_type!r}, {self.url!r})'
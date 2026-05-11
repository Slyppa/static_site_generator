class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        if self.value == None and self.children == None:
            raise Exception('value or children must exist')

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ''
        props_html = ''
        for prop in self.props:
            props_html += f" {prop}='{self.props[prop]}'"
        return props_html

    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f'{self.value}'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
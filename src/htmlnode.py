class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_htmml(self):
        html_text = ''
        for key in self.props:
            html_text += f' {key}={self.props[key]}'

        return f'{html_text}'
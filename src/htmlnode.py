class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        returned_string = " "
        for key in self.props:
            returned_string += f'{key}="{self.props[key]}" '
        return returned_string
    
    def __repr__(self):
        return f"TAG: {self.tag} VALUE: {self.value} CHILDREN: {self.children} PROPS: {self.props_to_html()}"
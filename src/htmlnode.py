class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # ""
        self.value = value          # ""
        self.children = children    # []
        self.props = props          # {}
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        # guard for nodes with no attributes
        if self.props is None:
            return ""
        all_attributes = ""
        for k, v in self.props.items():
            # note the leading space in the f-string
            all_attributes += f' {k}="{v}"'
        return all_attributes

    def __repr__(self):
        return f"""
    Tag: {self.tag}
    Value: {self.value}
    Children: {self.children}
    Props: {self.props}
    """


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        # guards
        if self.value is None:
            raise ValueError("Invalid HTML - there's no value")
        if self.tag is None:
            return self.value 
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        
    def __repr__(self):
        return f"""
LeafNode: {self.tag}, {self.value}, {self.props}
    """


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is None:
            raise ValueError("No children")
        
        children_as_string = ""
        child_html = [node.to_html() for node in self.children]
        for thing in child_html:
            children_as_string += thing

        return f"""<{self.tag}{self.props_to_html()}>{children_as_string}</{self.tag}>"""


    def __repr__(self):
        return f"ParentNode: {self.tag} | children: {self.children} | props: {self.props}"
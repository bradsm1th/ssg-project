class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # ""
        self.value = value          # ""
        self.children = children    # []
        self.props = props          # {}
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
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


test = HTMLNode("h1", "Amazing Test")
# print(test)

a_tag_test = HTMLNode("a", "click here", None, {"href": "https://www.google.com"})

# print(a_tag_test.props_to_html())
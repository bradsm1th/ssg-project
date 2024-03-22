import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Amazing Test")
        self.assertEqual("""
    Tag: h1
    Value: Amazing Test
    Children: None
    Props: None
    """, repr(node))

        
    def test_to_html(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com"})
        self.assertRaises(Exception, node.to_html())

    
    def test_props_to_html(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())

        
if __name__ == "__main__":
    unittest.main()
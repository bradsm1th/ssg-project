import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Amazing Test")
        self.assertEqual("""
    Tag: h1
    Value: Amazing Test
    Children: None
    Props: None
    """, repr(node))

        
    def test_to_html_props(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com"})
        
        # self.assertRaises(Exception, node.to_html())

        self.assertEqual(' href="https://www.google.com"', node.props_to_html())


    def test_to_html_no_children(self):
        node = LeafNode("h1", "Howdy!")
        self.assertEqual(node.to_html(), "<h1>Howdy!</h1>")
 
        
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Howdy!")
        self.assertEqual(node.to_html(), "Howdy!")
 
if __name__ == "__main__":
    unittest.main()
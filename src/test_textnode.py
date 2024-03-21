import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", 'bold')
        node2 = TextNode("This is a text node", 'bold')
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", 'bold')
        node2 = TextNode("This is a different text node", 'bold')
        self.assertNotEqual(node, node2)

    def test_none_and_default_none_equal(self):
        node = TextNode("This is a text node", 'bold', url=None)
        node2 = TextNode("This is a text node", 'bold')
        self.assertEqual(node, node2)

    def test_different_props_not_eq(self):
        node = TextNode("This is a text node", 'bold')
        node2 = TextNode("This is a text node", 'italic')
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a tester", "text", "1.1.1.1") 
        self.assertEqual("TextNode(This is a tester, text, 1.1.1.1)", repr(node))

if __name__ == "__main__":
    unittest.main()
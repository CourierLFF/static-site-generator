import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        new_node = HTMLNode("h1", "Header One", ["Child One", "Child Two"], props)
        self.assertTrue(new_node)
    
    def test_two(self):
        new_leafNode = LeafNode("p", "I am a paragraph!")
        self.assertTrue(new_leafNode.to_html())
    
    def test_two(self):
        new_leafNode = LeafNode("a", "I am a link!", {"href" : "https://www.google.com"})
        self.assertTrue(new_leafNode.to_html())
    
    def test_three(self):
        new_leafNode = LeafNode("p", None)
        self.assertRaises(ValueError)
    
    def test_four(self):
        new_leafNode = LeafNode(None, "I have no tag!")
        self.assertTrue(new_leafNode.to_html())

if __name__ == "__main__":
    unittest.main()
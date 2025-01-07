import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_five(self):
        new_leafNode = LeafNode("p", "I am a paragraph!")
        new_leafNode2 = LeafNode("a", "I am a link!", {"href" : "https://www.google.com"})
        new_ParentNode = ParentNode("div", [new_leafNode, new_leafNode2])
        self.assertTrue(new_ParentNode.to_html())
    
    def test_six(self):
        new_leafNode = LeafNode("p", "I am a paragraph!")
        new_leafNode2 = LeafNode("a", "I am a link!", {"href" : "https://www.google.com"})
        new_ParentNode = ParentNode("div", [new_leafNode, new_leafNode2])
        new_outer_leafNode = LeafNode("h1", "I'm outside!")
        new_ParentNode2 = ParentNode("div", [new_outer_leafNode, new_ParentNode], {"href" : "https://www.google.com"})
        self.assertTrue(new_ParentNode2.to_html())
        

if __name__ == "__main__":
    unittest.main()
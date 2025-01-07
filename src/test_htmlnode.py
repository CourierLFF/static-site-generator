import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        new_node = HTMLNode("h1", "Header One", ["Child One", "Child Two"], props)
        self.assertTrue(new_node)

if __name__ == "__main__":
    unittest.main()
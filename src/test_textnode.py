import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_one(self):
        node = TextNode("ouiwequfdoi34uwu43543", TextType.ITALIC)
        node2 = TextNode("ouiwequfdoi34uwu43543", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_two(self):
        node = TextNode("This is node one", TextType.CODE)
        node2 = TextNode("This is node two", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_three(self):
        node = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_four(self):
        node = TextNode("URL Node", TextType.NORMAL, None)
        node2 = TextNode("URL Node", TextType.NORMAL, None)
        self.assertEqual(node, node2)
    
    def test_five(self):
        node = TextNode("BootDev Node", TextType.NORMAL, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        node2 = TextNode("BootDev Node", TextType.NORMAL, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        self.assertEqual(node, node2)
    
    def test_six(self):
        node = TextNode("BootDev Node", TextType.NORMAL, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        node2 = TextNode("BootDev Node", TextType.NORMAL, "https://www.google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
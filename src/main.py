from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.NORMAL):
            return LeafNode(None, text_node.text)
        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        case(TextType.LINK):
            return LeafNode("a", text_node.text, {"href" : text_node.url})
        case(TextType.IMAGE):
            return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text})

def __main__():
    new_TextNode = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
    converted_TextNode = text_node_to_html_node(new_TextNode)
    print(converted_TextNode.to_html())

__main__()
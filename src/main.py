from textnode import TextNode, TextType

def __main__():
    new_TextNode = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(new_TextNode)

__main__()
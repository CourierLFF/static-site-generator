import re

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    block_list = list(filter(lambda x: x.strip(), block_list))
    for x in range(len(block_list)):
        block_list[x] = block_list[x].strip(" ")
    return block_list


def block_to_block_type(block):
    if block[0] == "#":
        return "Heading"
    elif block[0:3] == "```" and block[-3:] == "```":
        if block[3] != "`" and block[-4] != "`":
            return "Code"
    if block[0] == ">":
        if len(block.split("\n")) > 2:
            all_quote = False
            split_block = block.split("\n")
            split_block = list(filter(lambda x: x.strip(), split_block))
            split_block = list(map(lambda x: x.strip(" "), split_block))
            for splitted_block in split_block:
                if splitted_block[0] == ">":
                    all_quote = True
                else:
                    return "Normal"
            if all_quote:
                return "Quote"
        else:
            return "Quote"
    if block[0:2] == "* " or block[0:2] == "- ":
        if len(block.split("\n")) > 2:
            all_list = False
            split_block = block.split("\n")
            split_block = list(filter(lambda x: x.strip(), split_block))
            split_block = list(map(lambda x: x.strip(" "), split_block))
            for splitted_block in split_block:
                if splitted_block[0:2] == "* " or splitted_block[0:2] == "- ":
                    all_list = True
                else:
                    return "Normal"
            if all_list:
                return "Unordered List"
        else:
            return "Unordered List"
    if re.search(r"\d+", block[0]):
        if len(block.split("\n")) > 2:
            all_list = False
            list_counter = 1
            split_block = block.split("\n")
            split_block = list(filter(lambda x: x.strip(), split_block))
            split_block = list(map(lambda x: x.strip(" "), split_block))
            for splitted_block in split_block:
                if splitted_block[0:3] == f"{list_counter}. " or splitted_block[0:3] == f"{list_counter}. ":
                    all_list = True
                    list_counter += 1
                else:
                    return "Normal"
            if all_list:
                return "Ordered List"
        else:
            return "Ordered List"     
    return "Normal"


test_string = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    block_list = list(filter(lambda x: x.strip(), block_list))
    for x in range(len(block_list)):
        block_list[x] = block_list[x].strip(" ")
    return block_list


test_string = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

#print(markdown_to_blocks(test_string))
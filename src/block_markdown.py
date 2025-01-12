def markdown_to_blocks(markdown):
    block_list = markdown.split("\n")
    block_list = list(filter(lambda x: x.strip(), block_list))
    for x in range(len(block_list)):
        block_list[x] = block_list[x].strip(" ")
    print(block_list)
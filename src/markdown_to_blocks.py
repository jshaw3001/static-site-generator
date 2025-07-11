def markdown_to_blocks(markdown):
    clean_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            clean_blocks.append(stripped)
    return clean_blocks
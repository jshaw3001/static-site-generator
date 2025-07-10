from textnode import TextType, TextNode
from extract_markdown import extract_markdown_links, extract_markdown_images

def text_to_textnodes(text):
    start_node = TextNode(text, TextType.TEXT)
    delim_types = [("`", TextType.CODE), ("**", TextType.BOLD), ("_", TextType.ITALIC)]
    first_split = split_nodes_image([start_node])
    second_split = split_nodes_link(first_split)
    final_split = second_split
    for delim, type in delim_types:
        final_split = split_nodes_delimiter(final_split, delim, type)
    return final_split
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception(f"Invalid markdown, odd number of {delimiter}s")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown = node.text
        images = extract_markdown_images(markdown)
        for image_alt, image_link in images:
            sections = markdown.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            if image_alt != "":
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            markdown = sections[1]
        if markdown != "":
            new_nodes.append(TextNode(markdown, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown = node.text
        links = extract_markdown_links(markdown)
        for anchor_text, link in links:
            sections = markdown.split(f"[{anchor_text}]({link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            if anchor_text != "":
                new_nodes.append(TextNode(anchor_text, TextType.LINK, link))
            markdown = sections[1]
        if markdown != "":
            new_nodes.append(TextNode(markdown, TextType.TEXT))
    return new_nodes
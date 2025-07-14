from textnode import TextType, TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode
from split_nodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("TextType of node not handled")
        
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        type = block_to_block_type(block)
        children.append(create_html_node(block, type))
    return ParentNode("div", children)

def create_html_node(block, type):
    match type:
        case BlockType.PARAGRAPH:
            clean_text = block.replace('\n', ' ')
            return ParentNode("p", text_to_children(clean_text))
        case BlockType.HEADING:
            stripped = block.lstrip("#")
            count = len(block) - len(stripped)
            return ParentNode(f"h{count}", text_to_children(stripped[1:]))
        case BlockType.CODE:
           clean_content = block[3:-3]
           if clean_content.startswith('\n'):
                clean_content = clean_content[1:]
           text_node = TextNode(clean_content, TextType.TEXT)
           code_html = ParentNode("code", [text_node_to_html_node(text_node)])
           return ParentNode("pre", [code_html])
        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(remove_quote_markers(block)))
        case BlockType.UNORDERED_LIST:
            list_items = create_list_items(block)
            return ParentNode("ul", list_items)
        case BlockType.ORDERED_LIST:
            list_items = create_ordered_list_items(block)
            return ParentNode("ol", list_items)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def remove_quote_markers(text):
    lines = text.split("\n")
    clean = []
    for line in lines:
        clean.append(line[2:])
    return " ".join(clean)

def create_list_items(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(ParentNode("li", text_to_children(line[2:])))
    return children

def create_ordered_list_items(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        space_index = line.find('. ')
        content = line[space_index + 2:]  # +2 to skip '. '
        children.append(ParentNode("li", text_to_children(content)))
    return children

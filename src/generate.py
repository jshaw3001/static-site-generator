import os
from converters import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.exists(from_path):
        with open(from_path, "r") as f:
            markdown_text = f.read()
    else:
        raise Exception("Source markdown does not exist or path is invalid")
    if os.path.exists(template_path):
        with open(template_path, "r") as f:
            template_text = f.read()
    else:
        raise Exception("Source template does not exist or path is invalid")
    converted_markdown = markdown_to_html_node(markdown_text)
    html_content = converted_markdown.to_html()
    page_title = extract_title(markdown_text)
    html = template_text.replace("{{ Title }}", page_title)
    html = html.replace("{{ Content }}", html_content)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(html)

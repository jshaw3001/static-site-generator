from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered List"
    ORDERED_LIST = "Ordered List"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    heading_match = re.match(r"^(\#{1,6})(.)", block)
    if heading_match:
        if heading_match.group(2) == " ":
            return BlockType.HEADING
    if all_lines_start_with(lines, ">"):
        return BlockType.QUOTE
    if all_lines_start_with(lines, "- "):
        return BlockType.UNORDERED_LIST
    if check_ord_prefix(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def all_lines_start_with(lines, prefix):
    return all(line.startswith(prefix) for line in lines)

def check_ord_prefix(lines):
    for i in range(len(lines)):
        order_prefix = f"{i+1}. "
        if not lines[i].startswith(f"{order_prefix}"):
            return False
    return True

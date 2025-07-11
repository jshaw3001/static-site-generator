import unittest
from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_type_para(self):
        md = """
This is **bolded** paragraph
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.PARAGRAPH, type)

    def test_block_to_type_head(self):
        md = """
###### This is a heading block
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.HEADING, type)

    def test_block_to_type_code(self):
        md = """
```This is a
code block```
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.CODE, type)

    def test_block_to_type_quote(self):
        md = """
>This is a
>quote block
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.QUOTE, type)

    def test_block_to_type_unord(self):
        md = """
- This is an unordered
- list block
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.UNORDERED_LIST, type)

    def test_block_to_type_ord(self):
        md = """
1. This is an ordered
2. list block
3. that is getting
4. much longer
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.ORDERED_LIST, type)

    def test_block_to_type_empty(self):
        type = block_to_block_type("")
        self.assertEqual(BlockType.PARAGRAPH, type)

    def test_block_to_type_invalid_heading(self):
        md = """
####### This is an invalid heading block
"""
        blocks = markdown_to_blocks(md)
        type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.PARAGRAPH, type)
        
if __name__ == "__main__":
    unittest.main()

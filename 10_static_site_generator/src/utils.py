from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(textnode: TextNode) -> LeafNode:
    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=textnode.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=textnode.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=textnode.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=textnode.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=textnode.text, props={"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                value="",
                props={"alt": textnode.text, "src": textnode.url},
            )
        case _:
            raise Exception("Error: Invalid text_type conversion")

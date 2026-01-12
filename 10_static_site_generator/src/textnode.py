from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


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

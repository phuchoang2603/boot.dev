def converted_font_size(font_size):
    def inner_convert(doc_type):
        if doc_type == "txt":
            return font_size
        elif doc_type == "md":
            return font_size * 2
        elif doc_type == "docx":
            return font_size * 3
        else:
            raise ValueError("invalid doc type")

    return inner_convert

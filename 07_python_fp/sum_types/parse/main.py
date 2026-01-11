class MaybeParsed:
    pass


# don't touch above this line


class Parsed(MaybeParsed):
    def __init__(self, doc_name, text):
        super().__init__()
        self.doc_name = doc_name
        self.text = text


class ParseError(MaybeParsed):
    def __init__(self, doc_name, err):
        super().__init__()
        self.doc_name = doc_name
        self.err = err

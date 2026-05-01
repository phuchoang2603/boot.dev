class Trie:
    def find_matches(self, document):
        matches = set()
        for doc_index in range(len(document)):
            current = self.root
            for char_index in range(doc_index, len(document)):
                ch = document[char_index]
                if ch not in current:
                    break
                current = current[ch]
                if self.end_symbol in current:
                    matches.add(document[doc_index : char_index + 1])
        return matches

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

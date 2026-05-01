class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""

        while True:
            keys = list(current.keys())
            if self.end_symbol in keys:
                break
            if len(keys) > 1 or len(keys) == 0:
                break
            ch = keys[0]
            prefix += ch
            current = current[ch]

        return prefix

    # don't touch below this line

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

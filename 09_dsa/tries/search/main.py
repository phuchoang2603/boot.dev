class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)

        for key, value in sorted(current_level.items()):
            if key == self.end_symbol:
                continue
            prefix = current_prefix + key
            self.search_level(value, prefix, words)

        return words

    def words_with_prefix(self, prefix):
        words = []

        current = self.root

        for ch in prefix:
            if ch not in current:
                return []
            current = current[ch]

        return self.search_level(current, prefix, words)

    def exists(self, word):
        current = self.root

        for ch in word:
            if ch not in current:
                return False
            current = current[ch]

        if self.end_symbol in current:
            return True
        else:
            return False

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

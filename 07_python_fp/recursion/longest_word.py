def find_longest_word(document, longest_word=""):
    words = document.split()
    if len(words) == 0:
        return longest_word
    if len(words[0]) > len(longest_word):
        longest_word = words[0]
    return find_longest_word(" ".join(words[1:]), longest_word)

def count_words(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)


def count_char(file_contents: str) -> dict[str, int]:
    file_contents = file_contents.lower()
    chars = {}

    for char in file_contents:
        if not char.isalpha():
            continue

        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    return chars


def sort_on(items):
    return items["num"]


def sort_chars(chars: dict[str, int]) -> list[dict]:
    sorted_list = [
        {"char": char, "num": word_count} for char, word_count in chars.items()
    ]

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list

import sys
from stats import count_words, count_char, sort_chars


def get_book_text(filepath: str) -> str:
    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {count_words(file_contents)} total words")
    print("----------- Character Count --------")
    chars = sort_chars(count_char(file_contents))
    for char in chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

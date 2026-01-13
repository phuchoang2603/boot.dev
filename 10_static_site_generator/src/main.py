from utils import copy_files, generate_pages
from config import STATIC_DIR, PUBLIC_DIR, CONTENT_DIR


def main():
    try:
        copy_files(STATIC_DIR, PUBLIC_DIR)
        generate_pages(CONTENT_DIR, PUBLIC_DIR)
    except Exception as e:
        raise Exception(f"Error: {e}")


if __name__ == "__main__":
    main()

from utils import copy_files
from config import SRC_DIR, DES_DIR


def main():
    try:
        copy_files(SRC_DIR, DES_DIR)
    except Exception as e:
        raise Exception(f"Error: {e}")


if __name__ == "__main__":
    main()

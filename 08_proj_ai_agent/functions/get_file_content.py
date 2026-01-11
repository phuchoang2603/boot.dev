from config import MAX_CHARS
from functions.utils import create_path_validator

file_validator = create_path_validator(must_be="file", operation="read")


def get_file_content(working_directory, file_path):
    file_abspath = file_validator(working_directory, file_path)

    try:
        with open(file_abspath, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
    except Exception as e:
        raise Exception(f"Error: {e}")

    return file_content

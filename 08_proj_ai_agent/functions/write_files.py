import os
from functions.utils import create_path_validator

write_validator = create_path_validator(must_not_be="dir", operation="write")


def write_file(working_directory, file_path, content):
    file_abspath = write_validator(working_directory, file_path)

    parent_dir = os.path.dirname(file_abspath)
    os.makedirs(parent_dir, exist_ok=True)

    try:
        with open(file_abspath, "w") as f:
            f.write(content)
    except Exception as e:
        raise Exception(f"Error: {e}")

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

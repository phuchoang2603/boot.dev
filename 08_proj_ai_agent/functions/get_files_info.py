import os
from functions.utils import create_path_validator

dir_validator = create_path_validator(must_be="dir", operation="list")


def get_files_info(working_directory, directory="."):
    target_dir = dir_validator(working_directory, directory)

    target_dir_content = "\n"

    try:
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            target_dir_content += f" - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
    except Exception as e:
        raise Exception(f"Error: {e}")

    return target_dir_content

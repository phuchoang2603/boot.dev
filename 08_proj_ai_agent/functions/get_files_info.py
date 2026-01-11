import os
from functions.utils import create_path_validator
from google.genai import types

dir_validator = create_path_validator(must_be="dir", operation="list")
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


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

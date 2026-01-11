import os
from functions.utils import create_path_validator
from google.genai import types

write_validator = create_path_validator(must_not_be="dir", operation="write")

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file relative to the working directory. Creates parent directories if needed. Can create new files or overwrite existing ones.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


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

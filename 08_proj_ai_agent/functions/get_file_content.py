from config import MAX_CHARS
from functions.utils import create_path_validator
from google.genai import types

file_validator = create_path_validator(must_be="file", operation="read")

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a file relative to the working directory. Files larger than 10000 characters will be truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


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

import os
from functions.utils import create_path_validator
import subprocess
from google.genai import types

file_validator = create_path_validator(must_be="file", operation="execute")

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to the working directory with optional command-line arguments and returns the output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional command-line arguments to pass to the Python script",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    file_abspath = file_validator(working_directory, file_path)
    if not file_abspath.endswith("py"):
        raise Exception(f'Error: "{file_path}" is not a Python file')

    command = ["python", file_abspath]
    if args is not None:
        command.extend(args)

    try:
        process = subprocess.run(
            command,
            cwd=os.path.abspath(working_directory),
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception as e:
        raise Exception(f"Error: executing Python file: {e}")

    if process.returncode != 0:
        return f"Process exited with code {process.returncode}"
    elif not process.stderr and not process.stdout:
        return "No output produced"
    else:
        return f"STDOUT:{process.stdout}\nSTDERR:{process.stderr}"

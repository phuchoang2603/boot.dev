import os
from functions.utils import create_path_validator
import subprocess

file_validator = create_path_validator(must_be="file", operation="execute")


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

import os


def create_path_validator(must_be=None, must_not_be=None, operation="access"):
    """
    This factory function returns a customized validator function that:
    - Validates paths are within the permitted working directory
    - Optionally validates path type (file vs directory)
    - Optionally validates path is NOT a certain type (useful for write operations)

    Args:
        must_be: Type check - 'file', 'dir', or None (path must be this type)
        must_not_be: Type check - 'file', 'dir', or None (path must NOT be this type)
        operation: Operation name for error messages ('read', 'list', 'write', etc.)
    """

    def validator(working_directory, target_path):
        working_dir = os.path.abspath(working_directory)
        absolute_path = os.path.normpath(os.path.join(working_dir, target_path))

        # Check if path is within permitted working directory
        if os.path.commonpath([working_dir, absolute_path]) != working_dir:
            raise Exception(
                f'Error: Cannot {operation} "{target_path}" as it is outside the permitted working directory'
            )

        # Optional positive type checking (must be this type)
        if must_be == "file" and not os.path.isfile(absolute_path):
            raise Exception(
                f'Error: File not found or is not a regular file: "{target_path}"'
            )
        elif must_be == "dir" and not os.path.isdir(absolute_path):
            raise Exception(
                f'Error: Directory not found or is not a valid directory: "{target_path}"'
            )

        # Optional negative type checking (must NOT be this type)
        if must_not_be == "dir" and os.path.isdir(absolute_path):
            raise Exception(
                f'Error: Cannot {operation} to "{target_path}" as it is a directory'
            )
        elif must_not_be == "file" and os.path.isfile(absolute_path):
            raise Exception(
                f'Error: Cannot {operation} to "{target_path}" as it is a file'
            )

        return absolute_path

    return validator

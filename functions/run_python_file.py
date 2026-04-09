import os
import subprocess
from functions.verify_file_path import verify_file_path
def run_python_file(working_directory, file_path, args=None):
    if not verify_file_path(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    absolute_file_path = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
    command = ["python", absolute_file_path]
    if args:
        command.extend(args)

    try:
        result = subprocess.run(command, capture_output=True, text=True, cwd=working_directory)
        if result.returncode != 0:
            outputError = f'"Process exited with code X: {result.returncode}'
            if not result.stdout.strip() and not result.stderr.strip():
                outputError += "No output produced"
            return outputError
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

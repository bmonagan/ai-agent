import os 
from functions.verify_file_path import verify_file_path
def run_python_file(working_directory, file_path, args=None):
    if not verify_file_path(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
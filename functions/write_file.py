import os
from functions.verify_file_path import verify_file_path

def write_file(working_directory, file_path, content):
    valid_target_dir = verify_file_path(working_directory, file_path)
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    abs_file_path = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
    try:
        makedirs = os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'


import os 
from config import MAX_CHARS
from functions.verify_file_path import verify_file_path

def get_file_content(working_directory, file_path):
    valid_target_dir = verify_file_path(working_directory, file_path)

    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    abs_file_path = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
        
    try:
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
import os
from functions.verify_file_path import verify_file_path

def get_files_info(working_directory, directory="."):
    valid_target_dir = verify_file_path(working_directory, directory)
    
    
    print(f"Result for {directory if directory != "." else 'current directory'}")
    if not valid_target_dir:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    
    target_dir = os.path.normpath(os.path.join(os.path.abspath(working_directory), directory))
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
        

    files_info = []
    for entry in os.listdir(target_dir):
        entry_path = os.path.join(target_dir, entry)
        file_info = {
            "name": entry,
            "size": os.path.getsize(entry_path),
            "is_directory": os.path.isdir(entry_path),
        }
        file_info_str = f" - {file_info['name']}: file_size={file_info['size']} bytes, is_dir={file_info['is_directory']}"
        files_info.append(file_info_str)
   
    return "\n".join(files_info)
import os
from pathlib import Path
def get_files_info(working_directory, directory="."):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_directory = os.path.abspath(os.path.join(absolute_working_dir, directory))
    target_dir = os.path.normpath(os.path.join(absolute_working_dir, directory))
    valid_target_dir = os.path.commonpath([absolute_working_dir, target_dir]) == absolute_working_dir
    print(f"Result for {directory if directory != "." else 'current directory'}")
    if not valid_target_dir:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    
    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return

    files_info = []
    for entry in os.listdir(target_dir):
        entry_path = os.path.join(target_dir, entry)
        file_info = {
            "name": entry,
            "size": os.path.getsize(entry_path),
            "is_directory": os.path.isdir(entry_path),
        }
        file_info_str = f"  - {file_info['name']}: file_size={file_info['size']} bytes, is_dir={file_info['is_directory']}"
        files_info.append(file_info_str)
   
    for info in files_info:
        print(info)
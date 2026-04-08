import os
from pathlib import Path
def get_files_info(working_directory, directory="."):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_directory = os.path.abspath(os.path.join(absolute_working_dir, directory))
    target_dir = os.path.normpath(os.path.join(absolute_working_dir, directory))
    valid_target_dir = os.path.commonpath([absolute_working_dir, target_dir]) == absolute_working_dir
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a valid directory'

get_files_info("calculator")
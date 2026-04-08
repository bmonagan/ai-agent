import os
def verify_file_path(working_directory, file_path):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_directory = os.path.abspath(os.path.join(absolute_working_dir, file_path))
    abs_file_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
    valid_target_dir = os.path.commonpath([absolute_working_dir, abs_file_path]) == absolute_working_dir
    return valid_target_dir
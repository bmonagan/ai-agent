import os
def get_files_info(working_directory, directory="."):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_directory = os.path.abspath(os.path.join(absolute_working_dir, directory))
    target_dir = os.path.normpath(os.path.join(absolute_working_dir, directory))
    print(f"Working Directory: {absolute_working_dir}")
    print(f"Directory: {absolute_directory}")
    print(f"Target Directory: {target_dir}")


get_files_info("calculator")
import os
import subprocess
from functions.verify_file_path import verify_file_path
def run_python_file(working_directory, file_path, args=None):
    try:
        if not verify_file_path(working_directory, file_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        absolute_file_path = os.path.normpath(os.path.join(os.path.abspath(working_directory),file_path)) 
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)

    
        result = subprocess.run(command, capture_output=True, text=True, cwd=working_directory, timeout=30)
        if result.returncode != 0:
            outputError = f'Process exited with code: {result.returncode}'
            if not result.stdout and not result.stderr:
                outputError += "No output produced"
            return outputError
        else:  
            out = result.stdout
            err = result.stderr
            output = ""
            if out:
                output += f"Standard Output:\n{out}\n"
            if err:
                output += f"Standard Error:\n{err}\n"
            return output   
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

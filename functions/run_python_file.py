import os
import subprocess
from functions.verify_file_path import verify_file_path
from google.genai import types


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
                output += f"'STDOUT:\n{out}\n"
            if err:
                output += f"STDERR:\n{err}\n"
            return output   
            
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to the working directory and returns captured output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional command line arguments passed to the Python file",
            ),
        },
        required=["file_path"],
    ),
)
    

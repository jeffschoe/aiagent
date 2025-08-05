import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            #stdin=None, input=None,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            #capture_output=True, 
            #shell=False, 
            cwd=abs_working_directory, 
            timeout=30, 
            #check=True, 
            #encoding=None, 
            #errors=None, 
            text=True, 
            #env=None, 
            #universal_newlines=None
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")   

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
       
        if not output:
            return "No output produced."
        return "\n".join(output) 
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

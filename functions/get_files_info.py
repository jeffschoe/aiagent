import os

def get_files_info(working_directory, directory="."):
    # goal: accept a directory path, and return a string that 
    # represents the contents of that directory.
   

    full_directory = os.path.join(working_directory, directory)
    abs_working_direcotry = os.path.abspath(working_directory)
    abs_full_directory = os.path.abspath(full_directory)

    if abs_full_directory.startswith(abs_working_direcotry) is False:
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(abs_full_directory) is False:
        return f'Error: "{directory}" is not a directory'

    print(f"***DEBUG: working_directory = {working_directory}")
    print(f"***DEBUG: directory = {directory}")
    print(f"***DEBUG: full_path = {full_directory}")


    pass
    contents = ""

    return contents
import os

def get_files_info(working_directory, directory="."):
    full_directory = os.path.join(working_directory, directory)
    abs_working_direcotry = os.path.abspath(working_directory)
    abs_full_directory = os.path.abspath(full_directory)
    if abs_full_directory.startswith(abs_working_direcotry) is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(abs_full_directory) is False:
        return f'Error: "{directory}" is not a directory'

    try:
        contents_name_list = os.listdir(abs_full_directory)
        contents_full_info_list = []

        for content in contents_name_list:
            abs_content_path = os.path.join(abs_full_directory, content)
            full_info_string = f"- {content}: file_size={os.path.getsize(abs_content_path)} bytes, is_dir={os.path.isdir(abs_content_path)}"
            contents_full_info_list.append(full_info_string)
        full_contents_string = "\n".join(contents_full_info_list)

        return full_contents_string

    except Exception as e:
        return f"Error:{e}"

    
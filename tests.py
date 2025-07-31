from functions.get_files_info import get_files_info


def formatter(string):
    if string.startswith("-"):
        string_list = string.split('\n')
        spaced_string_list = []
        for str in string_list:
            spaced_string_list.append(f" {str}") # add leading space
        formatted_string = '\n'.join(spaced_string_list)
    elif string.startswith("Error"):
        formatted_string = f"    {string}" # add leading indent
    return formatted_string


def main():
    # current directory
    cd_string = get_files_info("calculator", ".")
    formatted_cd_string = formatter(cd_string)
    print("Result for current directory:\n" + 
        formatted_cd_string
        )


    # pkg
    pkg_string = get_files_info("calculator", "pkg")
    formatted_pkg_string = formatter(pkg_string)
    print("Result for 'pkg' directory:\n" +
        formatted_pkg_string
        )


    # /bin
    bin_string = get_files_info("calculator", "/bin")
    formatted_bin_string = formatter(bin_string)
    print("Result for '/bin' directory:\n" +
        formatted_bin_string
        )


    # ../
    parent_dir_string = get_files_info("calculator", "../")
    formatted_parent_dir_string = formatter(parent_dir_string)
    print("Result for '../' directory:\n" +
        formatted_parent_dir_string
        )


if __name__ == "__main__":
    main()


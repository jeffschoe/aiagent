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


def test():
    # current directory
    result = formatter(get_files_info("calculator", "."))
    print("Result for current directory:")
    print(result)

    # pkg
    result = formatter(get_files_info("calculator", "pkg"))
    print("Result for 'pkg' directory:")
    print(result)  

    # /bin
    result = formatter(get_files_info("calculator", "/bin"))
    print("Result for '/bin' directory:")
    print(result)

    # ../
    result = formatter(get_files_info("calculator", "../"))
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()


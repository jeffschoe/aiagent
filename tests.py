from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

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


    result = run_python_file("calculator", "main.py")
    print("Result for TEST 1:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for TEST 2:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result for TEST 3:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for TEST 4:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for TEST 5:")
    print(result)

    """

    # write file tests
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for TEST 1:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for TEST 2:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for TEST 3:")
    print(result)

    
    # get file content tests
    result = get_file_content("calculator", "main.py")
    print("Result for TEST 1:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for TEST 2:")
    print(result)

    result = get_file_content("calculator", "/bin/cat") 
    print("Result for TEST 3:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for TEST 4:")
    print(result)

    
    # get file info tests
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

    
    result = get_file_content("calculator", "lorem.txt")
    print("Result for get_file_content test:")
    print(result)
    """



if __name__ == "__main__":
    test()


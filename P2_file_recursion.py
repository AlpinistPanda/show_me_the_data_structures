import os


def find_files(suffix=None, path=None):
    """
    Finds all the files that is in a path folder
    that has a specific suffix
    This method also checks subdirectries

    Args:
      suffix(str): suffix of the file
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if path == None:
        return "Please input a path"
    elif suffix == None:
        return "Please input suffix"
    result = []
    try:
        files = os.listdir(path)
    except Exception as e:
        return "path not found"
    files = [os.path.join(path, file) for file in files]
    for file in files:
        if os.path.isfile(file) and file.endswith(suffix):
            result.append(file)
        if os.path.isdir(file):
            sub_result = find_files(suffix, file)
            result.extend(sub_result)
    return result


# should print all the py file from input dir
print(find_files('.py', '/'))
print(find_files('.py', ""))  # should return "path not found"
print(find_files('.py'))     # should return "Please input a path"
# should return "Please input suffix"
print(find_files(path='/'))

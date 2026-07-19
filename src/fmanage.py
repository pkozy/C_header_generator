import os
import string_helper

def __get_files(dir=".") -> list:
    """
    Returns a list of tuples of all the files in the given directory, containing:
        
    :param str dir: The directory to search
    :return list: List of tuples containing
        1. name of the file
        2. if it is a directory
    """

    files=[];
    for f in os.scandir(dir):
        fdata = (os.path.abspath(f.name), f.is_dir())
        files.append(fdata);
    return files;


def get_c_files(dir=".") -> list:
    """
    Returns a list of the paths to all the .c files from the input.
    
    :param str dir: The directory to search
    :return list: A list of the paths to all the .c files from the parameter.
    """

    files = __get_files(dir)
    c_files = []

    for f_tuple in files:
        fname = f_tuple[0]
        is_dir = f_tuple[1]
        if is_dir:
            os.chdir(fname)
            c_files += get_c_files()
            os.chdir("..")
        else:
            if string_helper.is_c_file(fname):
                c_files.append(fname)
    return c_files
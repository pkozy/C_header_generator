
"""
This module focuses on manipulating the files in the directory
to create the header.

Author: Polina Kozyarchuk
Version: 7/12/26
"""

import string_helper
import os

def main():
    print(get_c_files(get_files()))


def get_files(dir=".") -> list:
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


def get_c_files(files) -> list:
    """
    Returns a list of the paths to all the .c files from the input.
    
    :param list files: List of tuples (typically from get_files()) containing
        1. name of the file
        2. if it is a directory
    :return list: A list of the paths to all the .c files from the parameter.
    """

    c_files = []

    for f_tuple in files:
        fname = f_tuple[0]
        is_dir = f_tuple[1]
        if is_dir:
            os.chdir(fname)
            c_files += get_c_files(get_files())
            os.chdir("..")
        else:
            if string_helper.is_c_file(fname):
                c_files.append(fname)
    return c_files



if __name__ == "__main__":
    main()

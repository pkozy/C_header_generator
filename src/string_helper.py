"""
This module includes functions that help manipulate and identify strings.

Author: Polina Kozyarchuk
Version: 7/12/26
"""
import re

def is_c_file(file) -> bool:
    """
    Returns whether or not a file is a c file (if it ends in .c)
    * does not need to be absolute path

    :param str file: The name of the file
    :return bool: True if file is a c file, false otherwise
    """

    pattern = re.compile("^[^ .]+.c$") # excludes files with spaces and extra dots
    is_match = pattern.match(file)
    if is_match:
        return True
    else: 
        return False

def is_include(line) -> bool:
    pattern = re.compile("^#include <.+")
    is_match = pattern.match(line)
    if is_match:
        return True
    else:
        return False
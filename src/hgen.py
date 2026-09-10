import fmanage
import fgen
import os
import sys

"""
Header file generator for C files.

Author: Polina Kozyarchuk
Version: 7/12/26
"""

def main(): 
    input_type = sys.argv[1];
    if input_type == "d": 
        c_files = fmanage.get_c_files(sys.argv[2])
        for file in c_files:
            fgen.gen_h_file(file)
    elif input_type == "f":
        file = sys.argv[2]
        fgen.gen_h_file(file)
    else:
        print("How to use: python3 hgen.py [input type] [name of file/directory]\n [input type]: must be either \"d\" for directory or \"f\" for file\n [name of file/directory]: give the relative or absolute path to the file or directory")


if __name__ == "__main__":
    main()

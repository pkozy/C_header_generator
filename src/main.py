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
    c_files = fmanage.get_c_files(sys.argv[1])
   
    for file in c_files:
        fgen.gen_h_file(file)


if __name__ == "__main__":
    main()

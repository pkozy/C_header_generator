
This repository contains a python script that will generate header files for C programs. It is built using Tree-sitter, and is required for use.  

Download Tree-sitter from this repository:
https://github.com/tree-sitter/py-tree-sitter 

This script can be used with a single file or with a directory of files. Given a directory, it will create a header file for each C source code file: ensure that only code files have extension ".c" for the intended result.  

# How to use:  
`python3 hgen.py [input type] [name of file/directory]`  
[input type]: must be either \"d\" for directory or \"f\" for file.  
[name of file/directory]: give the relative or absolute path to the file or directory.  

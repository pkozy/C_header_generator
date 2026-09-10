import fmanage
import tree_sitter_c as tsc 
from tree_sitter import Language, Parser

def setup_trst(fpath): #-> TreeCursor:
    """
    Sets up tree sitter.

    :param str fpath: the file to use tree sitter on
    :return TreeCursor
    """
    C_LANGUAGE = Language(tsc.language())
    parser = Parser(C_LANGUAGE)

    sample = open(fpath, "r")
    src = sample.read()
    src_b = bytes(src, 'utf-8')

    tree = parser.parse(src_b)
    cursor = tree.walk()

    return cursor

def gen_h_file(fname) -> str:
    """
    Generates a header file for the given C file. Named the same as the C file
    with the extension .h. Found in the same directory as C file.

    :param str fname: (relative/abs) path to the C file.
    :return str: What was written to the header file
    """
    INCLUDES = 0
    FUNCTIONS = 1

    data = gen_h_statements(fname)

    hf_name = fname.split(".c")[0] + ".h"
    hfile = open(hf_name, "w")

    defname = fname.split("/")[-1] #xxx_h
    defname = defname.split(".c")[0] + "_h"

    to_write = "#ifndef " + defname + "\n#define " + defname + "\n\n"

    for inc in data[INCLUDES]:
        to_write += inc + "\n"
    to_write += "\n"

    for func in data[FUNCTIONS]:
        to_write += func + "\n"
    
    to_write += "\n#endif"

    hfile.write(to_write)
    hfile.close()

    return to_write

def gen_h_statements(fname) -> tuple:
    """
    Generates the statements that would be in a header file from the given 
    C file.

    :param str fname: The C file to search.
    :return tuple: (set: include statements, set: function declarations)
    """
    cursor = setup_trst(fname)

    # string sets
    includes = set()
    functions = set()

    cursor.goto_first_child()
    check_node(cursor.node, includes, functions)

    while(cursor.goto_next_sibling()):
        check_node(cursor.node, includes, functions)

    return((includes, functions))


def check_node(node, includes, functions):
    """
    Checks if a given node is an include or function statement, and adds it to the 
    corresponding set.

    :param Node node: The node to check.
    :param set includes: The set of include statements.
    :param set functions: The set of function declarations.
    """
    inc_txt = check_inc(node)
    func_txt = check_func(node)
    if (inc_txt != ""):
        includes.add(inc_txt)
    elif (func_txt != ""):
        functions.add(func_txt)

def check_inc(node) -> str:
    """
    Checks if a given node is an include statement, and returns the text of the node
    if it is. If the node is not an include statement, an empty String is returned.

    :param Node node: The node to check.
    :return str:    Empty String if the node is not an include statement,
                    Text of the node if it is an include statement.
    """
    txt = ""
    if (node.type == "preproc_include"):
        txt = node.text.decode('utf-8')
        txt = txt.strip()
    return txt

def check_func(node):
    """
    Checks if a given node is a function statement, and returns the text of the node
    if it is. If the node is not a function statement, an empty String is returned.

    :param Node node: The node to check.
    :return str:    Empty String if the node is not an include statement,
                    Text of the node if it is a function statement.
    """
    txt = ""
    if (node.type == "function_definition"):
        txt = node.text.decode('utf-8')
        txt = txt.replace("\n", "")
        txt = txt.split("{")[0]
        txt = txt.strip()
        txt += ";"
    return txt
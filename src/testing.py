import tree_sitter_c as tsc 
from tree_sitter import Language, Parser

C_LANGUAGE = Language(tsc.language())
parser = Parser(C_LANGUAGE)

sample = open("temp/sample.c", "r")
src = sample.read()
src_b = bytes(src, 'utf-8')

tree = parser.parse(src_b)
root = tree.root_node
#print(str(root))
cursor = tree.walk()

# start at translation_unit 

# go to first child
cursor.goto_first_child()

def check_inc(node):
    txt = ""
    if (node.type == "preproc_include"):
        txt = node.text.decode('utf-8')
        txt = txt.strip()
    return txt

def check_func(node):
    txt = ""
    if (node.type == "function_definition"):
        txt = node.text.decode('utf-8')
        txt = txt.replace("\n", "")
        txt = txt.split("{")[0]
        txt = txt.strip()
    return txt

print(check_func(cursor.node))
print(check_inc(cursor.node)) 

while(cursor.goto_next_sibling()):
    print(check_func(cursor.node)) 
    print(check_inc(cursor.node))   


"""
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()

# go to first child: type
cursor.goto_first_child()
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()

# go to second child: function declarator
cursor.goto_next_sibling()   
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()

# go to functions identifier
cursor.goto_first_child()
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()

# go to parameters
cursor.goto_next_sibling()
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()

# go to third child: body
cursor.goto_parent()  
cursor.goto_next_sibling()   
print(cursor.node.type)
print(cursor.field_name)
print(cursor.node.text)
print()
"""

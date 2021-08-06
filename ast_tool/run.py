import ast
import astpretty

file = ast.parse('importFrom.py')

def viewNode(node):
    astpretty.pprint(node)
    return

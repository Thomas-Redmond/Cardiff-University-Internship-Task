import ast
from _astErrorSuperClass import astError

class A705(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "A705"
        self._Text = "Pass the filename as an argument"
        self.generic_visit() # visit all child nodes of given node

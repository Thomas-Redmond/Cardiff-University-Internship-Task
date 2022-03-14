import ast

from src.Errors.RP01a00 import RP01a00 # Don't use global
from src.Errors.RP01a02 import RP01a02 # There should only be one argument
from src.Errors.RP01a03 import RP01a03 # Function should take an argument
from src.Errors.RP01a04 import RP01a04 # Do not use append for list concatenation
from src.Errors.RP01a05 import RP01a05 # Recommended function names not in use


class Router(ast.NodeVisitor):


    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages

        self.errorRecord = errorReporter

    def visit_Global(self, node):
        # During AST traversal if "global" keyword encountered

        #P719_runTest = P719(self.errorRecord, node)
        RP01a00_runTest = RP01a00(self.errorRecord, node)


    def visit_FunctionDef(self, node):
        # Durning AST Traversal if a function x(para1, para2) reached

        if node.name == 'program':
            RP01a02_runTest = RP01a02(self.errorRecord, node)
            RP01a03_runTest = RP01a03(self.errorRecord, node)

        else: pass
        self.generic_visit(node)

    def visit_Call(self, node):
        RP01a04_runTest = RP01a04(self.errorRecord, node)
        self.generic_visit(node)

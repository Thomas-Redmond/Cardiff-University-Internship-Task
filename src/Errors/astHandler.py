import ast

from src.Errors.RP01a00 import RP01a00 # Don't use global
from src.Errors.RP01a02 import RP01a02 # There should only be one argument for function program
from src.Errors.RP01a03 import RP01a03 # Function program should take an argument
from src.Errors.RP01a04 import RP01a04 # Do not use append for list concatenation
from src.Errors.RP01a05 import RP01a05 # Function parseList should take 2 arguments
from src.Errors.RP01a06 import RP01a06 # Function parseStr should take 2 arguments
from src.Errors.RP01a07 import RP01a07 # Function parseInt should take arguments


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

        elif node.name == 'parseList':
            RP01a05_runTest = RP01a05(self.errorRecord, node)
        elif node.name == 'parseStr':
            RP01a06_runTest = RP01a06(self.errorRecord, node)
        elif node.name == 'parseInt':
            RP01a07_runTest = RP01a07(self.errorRecord, node)

        else: pass
        self.generic_visit(node)

    def visit_Call(self, node):
        RP01a04_runTest = RP01a04(self.errorRecord, node)
        self.generic_visit(node)

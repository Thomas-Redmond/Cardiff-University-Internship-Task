import ast

# Question 1 + 2
from src.Errors.RP01a00 import RP01a00  # No to global
from src.Errors.RP01a01 import RP01a01  # For loop better here
from src.Errors.RP01a02 import RP01a02  # Only one arg
from src.Errors.RP01a03 import RP01a03  # There should be args
from src.Errors.RP01a04 import RP01a04  # Use append on list

# Question 2 only
from src.Errors.RP02a05 import Rp02a05  # Recursive Check

class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages

        self.errorRecord = errorReporter

    def visit_Global(self, node):
        # During AST traversal if "global" keyword encountered

        RP01a00(self.errorRecord, node)


    def visit_FunctionDef(self, node):
        # Durning AST Traversal if a function x(para1, para2) reached

        if node.name == 'program':
            # Test only interested on program namespace
            RP01a02(self.errorRecord, node) # Check arg list
            RP01a03(self.errorRecord, node) # Check there exists args

        elif node.name == 'listParser':
            # Test only interested on listParser namespace
            RP01a01(self.errorRecord, node)
            RP01a04(self.errorRecord, node)

        elif node.name == 'stringParser':
            # Test only interested on stringParser namespace


        elif node.name == 'intParser':
            # Test only interested on intParser namespace


        else: pass
        self.generic_visit(node)

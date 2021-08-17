import ast
from src.Axxx.P700 import P700
from src.Axxx.P702 import P702
from src.Axxx.P705 import P705
from src.Axxx.P714 import P714
from src.Axxx.P715 import P715

from src.Axxx.P717 import P717


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._reportHere = errorReporter

    def visit_FunctionDef(self, node):
        if node.name == 'game':
            P700_runTest = P700(self._reportHere, node)

        elif node.name == 'q1a':
            P702_runTest = P702(self._reportHere, node)

        elif node.name == 'readCSV':
            P705_runTest = P705(self._reportHere, node)

        elif node.name == 'plotWinProbabilities':
            P714_runTest = P714(self._reportHere, node)
            P715_runTest = P715(self._reportHere, node)

        elif node.name == 'winProbability':
            P717_runTest = P717(self._reportHere, node)

        else:
            pass
        self.generic_visit(node)

    def visit_Call(self, node):
        self.generic_visit(node)

"""
    def visit_Assign(self, node):
        print('Node type: Assign and fields: ', node._fields[0])
        self.generic_visit(node)

    def visit_BinOp(self, node):
        print('Node type: BinOp and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Expr(self, node):
        print('Node type: Expr and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Constant(self,node):
        print('Node type: Constant and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Import(self, node):
        print("Import visited")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        print("Import From visited")
        self.generic_visit(node)
"""

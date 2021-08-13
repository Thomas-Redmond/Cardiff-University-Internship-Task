import ast
from src.Axxx.P700 import P700
from src.Axxx.P702 import P702
from src.Axxx.P705 import P705
from src.Axxx.P714 import P714


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._reportHere = errorReporter
        self._testsToRun = ["P700", "P702", "P705", "P714"]

    def visit_FunctionDef(self, node):
        if "P700" in self._testsToRun and node.name == 'game':
            P700_runTest = P700(self._reportHere, node)
            self._testsToRun.remove("P700")
        elif "P702" in self._testsToRun and node.name == 'q1a':
            P702_runTest = P702(self._reportHere, node)
            self._testsToRun.remove("P702")
        elif "P705" in self._testsToRun and node.name == 'readCSV': # if Function name is readCSV
            P705_runTest = P705(self._reportHere, node)
            self._testsToRun.remove("P705")
        elif "P714" in self._testsToRun and node.name == 'plotWinProbabilities': # if Function name is readCSV
            P714_runTest = P714(self._reportHere, node)
            self._testsToRun.remove("P714")

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

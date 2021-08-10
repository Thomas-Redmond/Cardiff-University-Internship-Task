import ast
from src.Axxx.P705 import P705


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._reportHere = errorReporter

    def visit_FunctionDef(self, node):
        print(f'Node type: FunctionDef and fields {node._fields}')
        if node.name == 'readCSV':
            P705_runTest = P705(self._reportHere, node, node.lineno, node.col_offset)
        else:
            pass
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
"""
"""
    def visit_Import(self, node):
        print("Import visited")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        print("Import From visited")
        self.generic_visit(node)
"""

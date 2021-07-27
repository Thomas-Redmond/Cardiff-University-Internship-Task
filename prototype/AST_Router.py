import ast

class AST_Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._reportHere = errorReporter

    def visit_Import(self, node):
        print("Import visited")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        print("Import From visited")
        self.generic_visit(node)

    def visit_Assign(self, node):
        print('Node type: Assign and fields: ', node._fields[0])
        self.generic_visit(node)

    def visit_BinOp(self, node):
        print('Node type: BinOp and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Expr(self, node):
        print('Node type: Expr and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Num(self,node):
        print('Node type: Num and fields: ', node._fields)

    def visit_Name(self,node):
        print('Node type: Name and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Str(self, node):
        print('Node type: Str and fields: ', node._fields)

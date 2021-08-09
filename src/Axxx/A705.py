import ast
from src.Axxx._astErrorSuperClass import astError

class A705(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "A705"
        self._Text = "Pass the filename as an argument"
        print("Running")
        self.generic_visit(node) # visit all child nodes of given node

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

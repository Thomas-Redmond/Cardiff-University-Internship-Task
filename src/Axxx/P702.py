import ast
from src.Axxx._astErrorSuperClass import astError

class P702(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P702"
        self._Text = "Call the function for 1a"
        self._Loc = [lineno, col_offset]

    def run(self, node):
        """
        In Function q1a check that the random seed is set
        """
        try:
            pass
        except Exception as e:
            print(e)
            self.fail()
        return

    def visit_Call(self, node):
        
        self.generic_visit(node)

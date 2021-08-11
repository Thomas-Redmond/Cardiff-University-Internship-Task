import ast
from src.Axxx._astErrorSuperClass import astError

class P701(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P701"
        self._Text = "For loop is more appropiate"
        self._Loc = [lineno, col_offset]
        self.run(self._node)

    def run(self, node):
        """

        """
        try:

        except Exception as e:
            print(e)
            self.fail()
        return

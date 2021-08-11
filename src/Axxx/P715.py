import ast
from src.Axxx._astErrorSuperClass import astError

class P715(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P715"
        self._Text = "x axis should be ra/rb"
        self._Loc = [lineno, col_offset]
        self.run(self._node)

    def run(self, node):
        """

        """
        try:
            pass
        except Exception as e:
            print(e)
            self.fail()
        return
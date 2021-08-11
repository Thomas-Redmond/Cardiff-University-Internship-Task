import ast
from src.Axxx._astErrorSuperClass import astError

class P714(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P714"
        self._Text = "Sorting separately loses connection between input/output"
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

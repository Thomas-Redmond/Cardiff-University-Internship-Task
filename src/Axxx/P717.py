import ast
from src.Axxx._astErrorSuperClass import astError

class P717(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P717"
        self._Text = "Should be probability of winning a game"
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

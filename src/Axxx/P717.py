import ast
from src.Axxx._astErrorSuperClass import astError

class P717(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P717"
        self._Text = "Should be probability of winning a game"


    def run(self, node):
        """

        """
        try:

        except Exception as e:
            print(e)
            self.fail(self._lineno + node.lineno, node.col_offset)
        return

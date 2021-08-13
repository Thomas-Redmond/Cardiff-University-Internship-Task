import ast
from src.Axxx._astErrorSuperClass import astError

class P715(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P715"
        self._Text = "x axis should be ra/rb"


    def run(self, node):
        """

        """
        try:
            pass
        except Exception as e:
            print(e)
            self.fail(self._lineno + node.lineno, node.col_offset)
        return

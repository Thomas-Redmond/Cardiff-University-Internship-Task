import ast
from src.Axxx._astErrorSuperClass import astError

class P713(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P713"
        self._Text = "Need to sort data or only plot points to avoid untidy graph"


    def run(self, node):
        """

        """
        try:

        except Exception as e:
            print(e)
            self.fail(self._lineno + node.lineno, node.col_offset)
        return

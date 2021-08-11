import ast
from src.Axxx._astErrorSuperClass import astError

class P713(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P713"
        self._Text = "Need to sort data or only plot points to avoid untidy graph"
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

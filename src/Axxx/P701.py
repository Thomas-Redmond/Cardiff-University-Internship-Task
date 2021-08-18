import ast
from src.Axxx._astErrorSuperClass import astError

class P701(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P701"
        self._Text = "For loop is more appropriate in this function"

        self._reportHere.insertDefaultError(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        self.generic_visit(node)

    def visit_For(self, node):
        try:
            self.success() # for loop detected
            return

        except Exception as e:
            print(e)
            self.fail(node)

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

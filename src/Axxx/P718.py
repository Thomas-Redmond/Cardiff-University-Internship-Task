import ast
from src.Axxx._astErrorSuperClass import astError

class P718(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P718"
        self._Text = "Plot independant variable on the x - axis"

        # Error reported by default, successful test removes from list
        self._reportHere.insertDefaultError(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        self.generic_visit(node) # traverse child nodes in function q1a


    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.value.id == "plt" and node.func.attr == "plot": # # plt.plot
                if node.args[0].id == "x" and node.args[1].id == "y":
                    self.success()
                    return
                else:
                    return # test failed

        self.generic_visit(node)

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

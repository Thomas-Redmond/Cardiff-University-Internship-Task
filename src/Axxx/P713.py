import ast
from src.Axxx._astErrorSuperClass import astError

class P713(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P713"
        self._Text = "Need to sort data or only plot points"

        self._reportHere.insertDefaultError(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        self.generic_visit(node)

    def visit_Call(self, node):
        """
        Checks number of occurrences of sort in function > 1 fail
        """
        try:
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == "plot" and node.args[2].value == "o":
                    self.success()
                    return
            else:
                if node.func.id == "sorted":
                    self.success()
                    return
                else:
                    pass

            self.generic_visit(node)

        except Exception as e:
            print(e)
            self.fail(node)
        return

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

import ast
from src.Axxx._astErrorSuperClass import astError

class P715(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P715"
        self._Text = "X axis should be left column / right column"

        self.sortedDetected = 0
        self.generic_visit(node)

    def visit_Assign(self, node):
        """
        Checks number of occurrences of sort in function > 1 fail
        """
        try:
            print(f"Visited Assign: {ast.dump(node)}")
        except Exception as e:
            print(e)
            self.fail(node)
        return

import ast
from src.Axxx._astErrorSuperClass import astError

class P702(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P702"
        self._Text = "Call the function 'game' for 1a"
        self._Loc = [lineno, col_offset]

        # Error reported by default, successful test removes from list
        self._reportHere.insertDefaultError(self._Loc[0], self._Loc[1], self._Code + ": " + self._Text)
        self.generic_visit(node) # traverse child nodes in function q1a

    def visit_Call(self, node):
        if node.func.id == "game":
            print(f"{self._Code} success")
            self.success()
        else:
            print("failure")
            pass
        self.generic_visit(node)

    def success(self):
        self._reportHere.removeDefaultError()
        return

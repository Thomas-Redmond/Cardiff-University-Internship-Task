from from errorType import astError

class P717(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P717"
        self._Text = "Should be probability of winning a game"

        # Error reported by default, successful test removes from list
        self._reportHere.insertDefaultError(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        self.generic_visit(node) # traverse child nodes in function q1a

    def visit_Call(self, node):
        """
        Run test when encounters a function call ie winProbability(parameters)
        Test checks whether function call is to function named game
        Passes if so, removing error from location in self._reportHere
        """
        if isinstance(node.func, ast.Attribute):
            pass # ignore ast.Attribute nodes that are here by mistake
        else:
            if node.func.id == "game":
                self.success()
            else:
                pass
        self.generic_visit(node)

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

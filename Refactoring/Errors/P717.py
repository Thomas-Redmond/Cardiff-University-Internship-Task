from from errorType import astError

class P717(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._errorCode = "P717"
        self._errorText = "Should be probability of winning a game"

        self._failByDefault = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes


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

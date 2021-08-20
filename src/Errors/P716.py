from errorType import astError

class P716(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._errorCode = "P716"
        self._errorText = "Should be left column / right column"

        self._vars = [None, None]

        self._failByDefault = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes


    def visit_For(self, node):
        """
        Run test when encounters a function call ie winProbability(parameters)
        Test checks whether function call is to function named game
        Passes if so, removing error from location in self._reportHere
        """
        var1Col = node.target.elts[0].id    # save variable name of 1st column
        var2Col = node.target.elts[1].id    # save variable name of 2nd column
        self._vars = [var1Col, var2Col]      # store values in class scope
        self.generic_visit(node)            # Traversing child nodes


    def visit_BinOp(self, node):
        if (node.left.id == self._vars[0] and
            isinstance(node.op, ast.Div) and
            node.right.id == self._vars[1]):

            self.success()

        self.generic_visit(node)

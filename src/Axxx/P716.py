import ast
from src.Axxx._astErrorSuperClass import astError

class P716(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P716"
        self._Text = "Plot independant variable on the x - axis"

        self.vars = [None, None]

        # Error reported by default, successful test removes from list
        self._reportHere.insertDefaultError(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        self.generic_visit(node) # traverse child nodes in function q1a

    def visit_For(self, node):
        """
        Run test when encounters a function call ie winProbability(parameters)
        Test checks whether function call is to function named game
        Passes if so, removing error from location in self._reportHere
        """
        var1Col = node.target.elts[0].id # save variable name of 1st column
        var2Col = node.target.elts[1].id # save variable name of 2nd column
        self.vars = [var1Col, var2Col]
        self.generic_visit(node)


    def visit_BinOp(self, node):
        print(f"{ast.dump(node)}")
        print(f"{ast.dump(node.op)}")
        print(isinstance(node.op, ast.Div))
        if (node.left.id == self.vars[0] and
            isinstance(node.op, ast.Div) and
            node.right.id == self.vars[1]):

            self.success()
        self.generic_visit(node)

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

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

    def visit_For(self, node):
        """
        Run test when encounters a function call ie winProbability(parameters)
        Test checks whether function call is to function named game
        Passes if so, removing error from location in self._reportHere
        """
        var1Col = node.target.elts[0].id # save variable name of 1st column
        var2Col = node.target.elts[1].id # save variable name of 2nd column

        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.value.id == "x" and node.func.attr == "append": # x.append()
                y = []
                for x in node.args:
                    y.append(ast.dump(x))
                print(y)



        self.generic_visit(node)

    def visit_BinOp(self, node):
        print(f"{ast.dump(node)}")
        self.generic_visit(node)

    def success(self):
        """
        Remove error-by-default from list of errors
        """
        self._reportHere.removeDefaultError()
        return

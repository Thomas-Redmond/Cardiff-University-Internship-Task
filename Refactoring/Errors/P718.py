from from errorType import astError

class P718(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._errorCode = "P718"
        self._errorText = "Plot independant variable on the x - axis"

        self._failByDefault = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes


    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.value.id == "plt" and node.func.attr == "plot": # plt.plot()
                if node.args[0].id == "x" and node.args[1].id == "y":
                    self.success()
                    return  # End Test
                else:
                    return # Test Failed, end test

        self.generic_visit(node)    # Traverse child nodes

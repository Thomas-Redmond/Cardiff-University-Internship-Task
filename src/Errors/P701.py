import ast
from Errors.errorType import astError

class P701(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._errorCode = "P701"
        self._errorText = "For loop is more appropriate in this function"

        self._failByDefault = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes

    def visit_For(self, node):
        try:
            self.success() # for loop detected
            return

        except Exception as e:
            print(e)
            self.fail(node)

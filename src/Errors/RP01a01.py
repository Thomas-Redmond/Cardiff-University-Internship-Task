import ast
from src.Errors.errorType import astError

class Test(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "A001"
        self.errorText = "For loop is more appropriate in this function"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes

    def visit_For(self, node):
        try:
            self.success() # for loop detected
            return

        except Exception as e:
            print(e)
            self.fail(node)

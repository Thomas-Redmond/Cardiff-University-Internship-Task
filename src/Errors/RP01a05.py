import ast
from src.Errors.errorType import astError

class RP01a05(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "RP01a05"
        self.errorText = "Recommended Function names not in use"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes

    def visit_FunctionDef(self, node):
        try:
            if node.name == "program":
                self.success()
            return

        except Exception as e:
            print(e)
            #self.fail(node)

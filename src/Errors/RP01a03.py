import ast
from src.Errors.errorType import astError

class RP01a03(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "RP01a03"
        self.errorText = "Function should take an argument"

        self.run(node) # No need to traverse node further

    def run(self, node):
        """
        Fail if there is no arguments for the function
        """
        try:
            if len(node.args.args) >= 1: # testing number of parameters is at least 1
                self.success()
            else:
                self.fail(node)
        except Exception as e:
            print(e)
            #self.fail(node)
        return

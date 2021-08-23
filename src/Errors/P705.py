import ast
from Errors.errorType import astError

class P705(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._errorCode = "P705"
        self._errorText = "Pass the filename as an argument"

        self.run(node) # No need to traverse node further

    def run(self, node):
        """
        Checks number of parameters handed to readCSV function
        If at least one, passes test
        """
        try:
            if len(node.args.args) >= 1: # testing number of parameters is at least 1
                self.success()
            else:
                self.fail(node)
        except Exception as e:
            print(e)
            self.fail(node)
        return

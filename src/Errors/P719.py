import ast
from Errors.errorType import astError

class P719(astError):
# AST_Router encountered global keyword call
# Creates error instance with test unneccerrssary

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "P719"
        self.errorText = "Do not use Global"

        self.fail(node)

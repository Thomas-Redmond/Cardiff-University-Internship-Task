import ast
from src.Errors.errorType import astError

class Test(astError):
# AST_Router encountered global keyword call
# Creates error instance with test unneccerrssary

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "A000"
        self.errorText = "Do not use Global"

        self.fail(node)

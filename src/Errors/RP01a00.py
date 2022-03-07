import ast
from src.Errors.errorType import astError

class RP01a00(astError):
# AST_Router encountered global keyword call
# Creates error instance with test unneccerrssary

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "RP01a00"
        self.errorText = "Do not use Global"

        self.fail(node)

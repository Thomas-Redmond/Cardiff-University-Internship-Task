import ast
from src.Errors.errorType import astError

class P702(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "P702"
        self.errorText = "Call the function 'game' for 1a"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes


    def visit_Call(self, node):
        """
        Run test when encounters a function call ie question1(parameters)
        Test checks whether function call is to function named game
        Passes if so, removing error from location in self._reportHere
        """
        if isinstance(node.func, ast.Attribute):
            pass # ignore ast.Attribute nodes that are here by mistake
        else:
            if node.func.id == "game":
                self.success()
            else:
                pass
        self.generic_visit(node)

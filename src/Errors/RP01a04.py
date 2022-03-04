import ast
from src.Errors.errorType import astError

class Test(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "A005"
        self.errorText = "Use append for adding to lists"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)


    def visit_Call(self, node):
        """
        Use append when adding to lists
        """
        try:
            if isinstance(node.func):
                if node.func.attr == "append":
                    self.success()  # Remove errorBydefault from register
                    return          # Test continuing could accidently purge more errors than we want hence escape
                else:
                    pass # Error already recorded
            else:
                pass

        except Exception as e:
            self.fail(node)
        return

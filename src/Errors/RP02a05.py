import ast
from src.Errors.errorType import astError

class RP02a05(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "RP02a05"
        self.errorText = "Best practise is to make the function recursive"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)


    def visit_Call(self, node):
        """
        Checks if function functionName is called recursively
        """
        try:
            if isinstance(node.func):
                if node.func.value.id == "functionName":
                    self.success()  # Remove errorBydefault from register
                    return          # Test continuing could accidently purge more errors than we want hence escape
                else:
                    pass # Error already recorded
            else:
                pass

        except Exception as e:
            print(e)
            #self.fail(node)
        return

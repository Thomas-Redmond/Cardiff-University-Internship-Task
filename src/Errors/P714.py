import ast
from src.Errors.errorType import astError

class P714(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "P714"
        self.errorText = "Sorting separately loses connection between input/output"

        self.sortedDetected = 0     # Keeps track of use of sorted() in file
        self.generic_visit(node)    # Traverse Child Nodes

    def visit_Call(self, node):
        """
        Checks number of occurrences of sort in function > 1 fail
        """
        try:
            if isinstance(node.func, ast.Attribute):
                pass
            else:
                if node.func.id == "sorted":
                    self.sortedDetected += 1
                    if self.sortedDetected > 1: self.fail(node)
                    else: pass
                else: pass
        except Exception as e:
            print(e)
            self.fail(node)
        return

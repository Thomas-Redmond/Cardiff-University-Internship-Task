import ast
from src.Axxx._astErrorSuperClass import astError

class P714(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P714"
        self._Text = "Sorting separately loses connection between input/output"

        self.sortedDetected = 0
        self.generic_visit(node)

    def visit_Call(self, node):
        """
        Checks number of occurrences of sort in function > 1 fail
        """
        try:
            print(f"node is {ast.dump(node)}")
            if isinstance(node.func, ast.Attribute):
                pass
            else:
                if node.func.id == "sorted":
                    self.sortedDetected += 1
                    print("Found sorted")
                    if self.sortedDetected > 1:
                        self.fail(node)
                    else:
                        pass
                else:
                    pass
        except Exception as e:
            print(e)
            self.fail(node)
        return

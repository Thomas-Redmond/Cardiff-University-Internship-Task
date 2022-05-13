import ast
from src.Errors.errorType import astError

class RP01a04(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "RP01a04"
        self.errorText = "Do not use append for List Concatenation"

        # Not needed as not traversing child nodes
        self.generic_visit(node)
        #self.runTest(node)


    def visit_Call(self, node):
        """
        Do not use append when adding to lists
        """
        try:
            if node.func.attr == 'append' and isinstance(node.args[0], ast.List):
                self.fail(node)
            else:
                pass

        except Exception as e:
            print(e)
            #print(ast.dump())
            #self.fail(node)
        return

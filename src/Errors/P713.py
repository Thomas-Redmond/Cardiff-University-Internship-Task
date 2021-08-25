import ast
from Errors.errorType import astError

class P713(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self.errorCode = "P713"
        self.errorText = "Need to sort data or only plot points"

        self.failByDefaultVar = True  # Guilty-until-proven-innocent
        self.failByDefault(node)    # Add Error to record

        self.generic_visit(node)    # Begin traversing child nodes


    def visit_Call(self, node):
        """
        Checks number of occurrences of sort in function > 1 fail
        """
        try:
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == "plot" and node.args[2].value == "o":
                    self.success()
                    return # end test
            else:
                if node.func.id == "sorted":
                    self.success()
                    return # end test
                else:
                    pass

            self.generic_visit(node) # Traverse Child Nodes

        except Exception as e:
            print(e)
            self.fail(node)
        return

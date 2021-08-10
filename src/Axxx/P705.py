import ast
from src.Axxx._astErrorSuperClass import astError

class P705(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P705"
        self._Text = "Pass the filename as an argument"
        self._Loc = [lineno, col_offset]
        self.run(self._node)

    def run(self, node):
        """
        Checks number of parameters handed to readCSV function
        If at least one, passes test
        """
        try:
            if len(node.args.args) >= 1: # testing number of parameters is at least 1
                self.success()
                # perhaps also test that the parameter name is informative?
            else:
                self.fail()
        except Exception as e:
            print(e)
            self.fail()
        return

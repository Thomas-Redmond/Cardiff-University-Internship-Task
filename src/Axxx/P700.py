import ast
from src.Axxx._astErrorSuperClass import astError

class P700(astError, ast.NodeVisitor):

    def __init__(self, reportHere, node, lineno, col_offset):
        super().__init__(reportHere, node)
        self._Code = "P700"
        self._Text = "Only use the seed for debugging / testing OUTSIDE the function"
        self._Loc = [lineno, col_offset]
        self.generic_visit(node)

    def visit_Call(self, node):
        """
        Tests if random.seed is used inside function game
        """
        try:
            if isinstance(node.func, ast.Attribute):
                if node.func.value.id == "random" and node.func.attr == "seed":
                    # if function call is random.seed then fail
                    self._Loc = [self._Loc[0] + node.lineno, self._Loc[1] + node.col_offset]
                    self.fail()
                else:
                    pass
            else:
                pass

        except Exception as e:
            print(e)
            self.fail()
        return

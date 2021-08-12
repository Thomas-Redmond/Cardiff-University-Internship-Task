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
                pass
            else:
                if node.func.id == 'random' and node.func.attr == 'seed':
                    print(f"{self._Code} test failed")
                    self._Loc = [self._Loc[0] + 0, self._Loc[1] + 0] 
                    self.fail()
                else:
                    print(f"{self._Code} test passed")
                    self.success()

        except Exception as e:
            print(e)
            self.fail()
        return

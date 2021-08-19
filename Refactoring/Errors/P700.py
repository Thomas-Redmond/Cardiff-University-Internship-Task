from from errorType import astError

class P700(astError):

    def __init__(self, reportHere, node):
        super().__init__(reportHere, node)
        self._Code = "P700"
        self._Text = "Only use the seed for debugging / testing OUTSIDE the function"
        self.generic_visit(node)

    def visit_Call(self, node):
        """
        Tests if random.seed is used inside function game
        """
        try:
            if isinstance(node.func, ast.Attribute):
                if node.func.value.id == "random" and node.func.attr == "seed":
                    # if function call is random.seed then fail
                    self.fail(node)
                else:
                    pass
            else:
                pass

        except Exception as e:
            self.fail(node)
        return

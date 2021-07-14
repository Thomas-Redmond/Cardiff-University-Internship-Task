# AST.Visitor Class
# imported into COMSC_Plugin for checking each AST node

import ast

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def visit_game(self, node: ast.Call) -> None:
        for keyword in node.keywords:
            

        self.generic_visit(node) # checks child nodes

    # Recursive descent tree traversal
    def visit_Call(self, node: ast.Call) -> None:
        # visit_* where Call is a named part of the ast used in tutorial
        # Checking for specific tutorial case
        for keyword in node.keywords:
            if(
                    keyword.arg is None and
                    isinstance(keyword.value, ast.Dict) and
                    all(
                        isinstance(key, ast.Str)
                        for key in keyword.value.keys
                    ) and
                    all(
                        key.s.isidentifier()
                        for key in keyword.value.keys
                    )
            ):
                self.problems.append((node.lineno, node.col_offset))

        # last function of visits methods
        self.generic_visit(node)

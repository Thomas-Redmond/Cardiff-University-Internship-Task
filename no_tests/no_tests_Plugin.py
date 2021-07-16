"""
Plugin
"""

import ast
import sys

from typing import Generator
from typing import Tuple
from typing import Type
from typing import List
from typing import Any

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int, String]] = []

    def visit_Import(self, node):
        print("Import visited")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        print("Import From visited")
        self.generic_visit(node)

    def visit_Assign(self, node):
        print('Node type: Assign and fields: ', node._fields)
        self.generic_visit(node)

    def visit_BinOp(self, node):
        print('Node type: BinOp and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Expr(self, node):
        print('Node type: Expr and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Num(self,node):
        print('Node type: Num and fields: ', node._fields)

    def visit_Name(self,node):
        print('Node type: Name and fields: ', node._fields)
        self.generic_visit(node)

    def visit_Str(self, node):
        print('Node type: Str and fields: ', node._fields)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col, error_msg in visitor.problems:
            yield line, col, error_msg, type(self)

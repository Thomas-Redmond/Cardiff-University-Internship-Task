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
        csv_detected = False

        for alias in node.names:
            if alias.name == "csv":
                csv_detected = True
        if csv_detected == False:
            assert{"1, 1, No CSV file detected"}
        self.generic_visit(node)


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

import ast
import sys

import ASTHandler

from typing import Generator
from typing import Tuple
from typing import Type
from typing import Any

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Plugin:
    # display plugin information in help messaging
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = ASTHandler.Visitor()
        visitor.visit(self._tree)
        # for line, col in visitor.problems:
        #     yield line, col, 'X1 Error', type(self)
        yield 1, 1,  'X1 Error', type(self)

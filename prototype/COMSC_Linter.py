import sys
import ast

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

from typing import Generator
from typing import Tuple
from typing import Type
from typing import Any

# importing code I have written
import reportError# place to record errors
import AST_Router # Handles AST navigation for AST errors
import Unit_Testing # handles "PyTest" style errors
import Squash

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        """

        """

        self._tree = tree
        self._reportError = reportError.Reporter()
        self._routerAST = AST_Router.Router(self._reportError)
        self._testUnit = Unit_Testing.Controller(self._reportError)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Begin testing the program

        """

        # self._routerAST.visit(self._tree) # will send AST to begin traversal
        self._testUnit.run()
        self._reportError.displayRecord()
        yield 1, 1,  'X1 Error', 5 # issue 5, yield blocks a NoneType iterable error
        return

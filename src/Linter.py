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

import .errorReporter
import AST_Router
import Unit_Testing

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree
        self._errorRecord = errorReporter.Reporter()
        self._routerAST = AST_Router.Router(self._errorRecord)
        self._testUnit = Unit_Testing.Controller(self._errorRecord)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Starts the Plugin.
        Runs the various tests and yields the detected errors.
        """

        print(f"Running checks")
        self._routerAST.visit(self._tree) # will send AST to begin traversal
        self._testUnit.run()
        for [line, col, error] in self._errorRecord._record:
             yield line, col, error, "Plugin Error"
        return

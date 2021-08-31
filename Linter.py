import sys
import ast

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

from pathlib import Path
from typing import Generator
from typing import Tuple
from typing import Type
from typing import Any

from src import errorReporter
from src import AST_Router
from src import Unit_Testing
from src import sysArgParser

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self.tree = tree
        self.parser = sysArgParser.parser()
        self.errorRecord = errorReporter.Reporter()
        self.routerAST = AST_Router.Router(self.errorRecord)
        self.testUnit = Unit_Testing.Controller(self.errorRecord)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Starts the Plugin.
        Runs the various tests and yields the detected errors.
        """
        print(f"Running Linter tests")
        self.routerAST.visit(self.tree) # will send AST to begin traversal
        self.testUnit.run()
        for [line, col, error] in self.errorRecord.record:
             yield line, col, error, "Plugin Error"
        return

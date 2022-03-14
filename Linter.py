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

import src # handles import of src/*.py files

class Plugin:
    # Flake8 Plugin variables

    name = __name__
    version = importlib_metadata.version(__name__)
    #off_by_default = True

    def __init__(self, tree: ast.AST):

        self.tree = tree
        self.parser = src.parser()
        self.errorRecord = src.Reporter()

        # Various types of tests
        self.funcCheck = src.funcCheck(self.errorRecord)
        self.routerAST = src.Router(self.errorRecord)
        self.testUnit = src.TestCases(self.errorRecord)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        # Starts the Plugin.
        # Runs the various tests and yields the detected errors.

        print("------------------")
        print(f"{self.name} {self.version} Installed") # states Plugin installed - does not indicate whether user has allowed use
        print(f"To use: flake8 absolute/path/to/filename.py")
        print("------------------")

        if self.funcCheck.activated != True:
            # If required function names not in use tests will not work
            # Other tests are only possible if all function names in use

            self.testUnit.run() # Run pytest style tests, first being P799
            self.routerAST.visit(self.tree) # Start AST node traversal

        for [line, col, error] in self.errorRecord.record:
            yield line, col, error, "Plugin Error" # output all errors in program
        return

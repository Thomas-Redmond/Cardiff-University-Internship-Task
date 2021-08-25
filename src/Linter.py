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

def addSRC2Path():
    try:
        fileDirectory = Path(__file__).parent
        fileDirectoryParts = fileDirectory.parts
        if 'lib' in fileDirectoryParts:
            indexLib = fileDirectoryParts.index('lib')
            newPath = Path()

            for addressComponent in fileDirectoryParts:
                if addressComponent != 'lib':
                    newPath = newPath.joinpath(addressComponent)
                else:
                    newPath = newPath.parent # strip last directory before lib out of address
                    print(newPath)
                    break

        # else:
        #     raise Exception("Virtual Environment not in use")
        sys.path.insert(0, str(newPath)) # add installation folder to path
        print(f"Added file location {newPath} to Path")
    except ModuleNotFoundError:
        print(f"Importing source files failed using path {newPath} given {Path(__file__).parent}")
        print(f"Traceback {e}")

addSRC2Path()
from src import errorReporter
from src import AST_Router
from src import Unit_Testing

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self.tree = tree
        self.parser = ""
        self.errorRecord = errorReporter.Reporter()
        self.routerAST = AST_Router.Router(self.errorRecord)
        self.testUnit = Unit_Testing.Controller(self.errorRecord)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Starts the Plugin.
        Runs the various tests and yields the detected errors.
        """

        print(f"Running checks")
        self.routerAST.visit(self.tree) # will send AST to begin traversal
        self.testUnit.run()
        for [line, col, error] in self.errorRecord.record:
             yield line, col, error, "Plugin Error"
        return

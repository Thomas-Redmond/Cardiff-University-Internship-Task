import sys
import ast
from pathlib import Path

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

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


        sys.path.insert(0, str(newPath)) # add installation folder to path
        print(f"Added file location {newPath} to Path")
    except ModuleNotFoundError:
        print(f"Importing source files failed using path {newPath} given {Path(__file__).parent}")
        print(f"Traceback {e}")

try: # importing code I have written
    addSRC2Path() # add my code to front of path
    import src.reportError as re    # place to record errors
    import src.AST_Router as ar     # Handles AST navigation for AST errors
    import src.Unit_Testing as ut   # handles "PyTest" style errors
except Exception as e:
    raise ModuleNotFoundError(f"Importing source files failed using path {newPath} given {Path(__file__).parent}")
    print(e)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree
        self._reportError = re.Reporter()
        self._routerAST = ar.Router(self._reportError)
        self._testUnit = ut.Controller(self._reportError)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Starts the Plugin.
        Runs the various tests and yields the detected errors.
        """

        self._routerAST.visit(self._tree) # will send AST to begin traversal
        self._testUnit.run()
        for [line, col, error] in self._reportError._record:
             yield line, col, error, "Plugin Error"
        return

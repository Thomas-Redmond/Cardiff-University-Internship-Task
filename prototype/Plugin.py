import sys
import ast

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

import AST_Router
import reportError

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        """

        """

        self._tree = tree
        self._reportError = reportError()
        self._routerAST = AST_Router(self._reportError)
        self._testUnit = Unit_Testing(self._reportError)

    def run(self):
        """
        Begin testing the program

        """
        return

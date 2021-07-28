import sys
import ast

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

# importing code I have written
import reportError # place to record errors
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

    def run(self):
        """
        Begin testing the program

        """
        self._routerAST.visit(self._tree) # will send AST to begin traversal
        return

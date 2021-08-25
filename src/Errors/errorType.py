# File is for generic type errors
import ast
import sys
from pathlib import Path

class specialCase:
    def __init__(self):
        self.filename = Path(sys.argv[1])
        self.Squash = __import__(self.importModule(self.filename))

    def importModule(self, filename):
        # Tests if filename parameter exists given complete address
        # Raises ModuleNotFoundError otherwise
        # Adds parent directory to path and returns filename stem
        if Path.exists(filename):
            sys.path.insert(0, str(filename.parent))
            return filename.stem
        else:
            raise ModuleNotFoundError(f"Address {filename} was not found")


class basicError:
    def __init__(self, reportHere):
        self._errorRecord = reportHere  # Reference to object
        self._failByDefault = False     # Will error be recorded on start ?
        self._errorCode = "Pxxx"
        self._errorText = "Example Error"

    def fail(self): # Overriden by child class
        # Appends details of failed test to Reporter obj referenced by self._errorRecord
        self._errorRecord.setRecord(0, 0, self._errorCode + ": " + self._errorText)

    def failByDefault(self): # Overriden later
        # Inserts Error at beginning to be removed later (Guilty until proven innocent)
        if self._failByDefault == True:
            self._errorRecord.insertDefaultError(0, 0, self._errorCode + ": " + self._errorText)
        else:
            raise UserWarning("This is not a Fail-By-Default error")

    def success(self):
        # remove errorByDefault if true otherwise does nothing
        if self._failByDefault == True:
            self._errorRecord.removeDefaultError()
        else: pass


class astError(basicError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere)

    def fail(self, node): # Overrides basicError version
        # Appends details of failed test to Reporter obj referenced by self._errorRecord
        self._errorRecord.setRecord(node.lineno, node.col_offset, self._errorCode + ": " + self._errorText)

    def failByDefault(self, node): # Override
        # Inserts Error at beginning to be removed later (Guilty until proven innocent)
        if self._failByDefault == True:
            self._errorRecord.insertDefaultError(node.lineno, node.col_offset, self._errorCode + ": " + self._errorText)
        else:
            raise UserWarning("This is not a Fail-By-Default error")

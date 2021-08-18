# File is for generic type errors
import ast

class basicError:
    def __init__(self, reportHere):
        self._errorRecord = reportHere  # Reference to object
        self._failByDefault = False     # Will error be recorded on start ?
        self._errorCode = ""
        self._errorText = ""

    def fail(self): pass # Overriden later

    def failByDefault(self): pass # Overriden later

    def success(self):
        # remove errorByDefault if true otherwise does nothing
        if self._failByDefault == True:
            self._errorRecord.removeDefaultError()
        else: pass

class utError(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)

    def fail(self):
        """
        Appends details of failed test to Record in class Reporter
        [Temp] Notifies user of failure
        """
        self._reportHere.setRecord(0, 0, self._Code + ": " + self._Text)


class astError(basicError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere)

        self.generic_visit()

    def fail(self, node):
        """
        Add error report to self._reportHere Reporter class
        """
        self._reportHere.setRecord(node.lineno, node.col_offset, self._Code + ": " + self._Text)

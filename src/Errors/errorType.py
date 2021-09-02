# File is for generic type errors
import ast

class basicError:
    def __init__(self, reportHere):
        self.errorRecord = reportHere  # Reference to object
        self.failByDefaultVar = False     # Will error be recorded on start ?
        self.errorCode = "Pxxx"
        self.errorText = "Example Error"

    def fail(self): # Overriden by child class
        # Appends details of failed test to Reporter obj referenced by self._errorRecord
        self.errorRecord.setRecord(0, 0, self.errorCode + ": " + self.errorText)

    def failByDefault(self): # Overriden later
        # Inserts Error at beginning to be removed later (Guilty until proven innocent)
        if self.failByDefaultVar == True:
            self.errorRecord.insertDefaultError(0, 0, self.errorCode + ": " + self.errorText)
        else:
            raise UserWarning("This is not a Fail-By-Default error")

    def success(self):
        # remove errorByDefault if true otherwise does nothing

        if self.failByDefaultVar == True:
            self.errorRecord.removeDefaultError()
        else: pass


class astError(basicError, ast.NodeVisitor):

    def __init__(self, reportHere, node):
        super().__init__(reportHere)

    def fail(self, node): # Overrides basicError version
        # Appends details of failed test to Reporter obj referenced by self._errorRecord
        self.errorRecord.setRecord(node.lineno, node.col_offset, self.errorCode + ": " + self.errorText)

    def failByDefault(self, node): # Override
        # Inserts Error at beginning to be removed later (Guilty until proven innocent)
        if self.failByDefaultVar == True:
            self.errorRecord.insertDefaultError(node.lineno, node.col_offset, self.errorCode + ": " + self.errorText)
        else:
            raise UserWarning("This is not a Fail-By-Default error")

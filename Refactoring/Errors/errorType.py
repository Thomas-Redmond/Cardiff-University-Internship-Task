# File is for generic type errors

class basicError:
    def __init__(self, reportHere):
        self._errorRecord = reportHere  # Reference to object
        self._failByDefault = False     # Will error be recorded on start

        failByDefault()

    def fail(self): pass

    def failByDefault(self):
        if self._failByDefault == True:
            self._errorRecord.insertDefaultError()

    def success(self): pass

class PluginError:

    def __init__(self, reportHere):
        self._reportHere = reportHere
        self._Loc = [0, 0]

    def run(self): pass # Overridden by Child class

    def success(self): pass

    def fail(self):
        """
        Appends details of failed test to Record in class Reporter
        [Temp] Notifies user of failure
        """
        self._reportHere.setRecord(self._Loc[0], self._Loc[1], self._Code + ": " + self._Text)
        print(f"{self._Code} Failed")
        return

class astError:

    def __init__(self, reportHere, node):
        self._reportHere = reportHere

    def run(self): pass

    def success(self): pass

    def fail(self, node):
        """
        Add error report to self._reportHere Reporter class
        """
        self._reportHere.setRecord(node.lineno, node.col_offset, self._Code + ": " + self._Text)

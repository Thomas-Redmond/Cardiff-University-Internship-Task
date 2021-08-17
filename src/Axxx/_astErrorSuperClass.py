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

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        print(f'Loc: {self._Loc[0], self._Loc[1]}')
        return

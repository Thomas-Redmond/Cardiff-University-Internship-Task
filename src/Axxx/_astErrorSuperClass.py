class astError:

    def __init__(self, reportHere, node):
        self._reportHere = reportHere

    def run(self): pass

    def success(self):
        for error in self._reportHere._record:
            print(error, 'comparing against' , [0, 0, f"{self._Code}: {self._Text}"])
            if error == [0, 0, f"{self._Code}: {self._Text}"]:
                print(f"Removing error {error}")
                self._reportHere.record.remove(error)
                return

    def fail(self, node):
        """
        Add error report to self._reportHere Reporter class
        """
        self._reportHere.setRecord(node.lineno, node.col_offset, self._Code + ": " + self._Text)
        # self.lineno + lineno      takes lineno of original tree + offset by new tree

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        print(f'Loc: {self._Loc[0], self._Loc[1]}')
        return

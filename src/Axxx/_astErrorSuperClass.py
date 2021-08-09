class astError:

    def __init__(self, reportHere, node):
        self._reportHere = reportHere
        self._node = node
        self._Loc = [0, 0]

    def run(self): pass

    def success(self): pass

    def fail(self):
        self._reportHere.setRecord(self._Loc[0], self._Loc[1], self._Code + ": " + self._Text)
        print(f"{self._Code} Failed")

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        print(f'Loc: {self._Loc[0], self._Loc[1]}')
        return

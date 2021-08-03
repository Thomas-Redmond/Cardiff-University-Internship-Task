class Reporter:

    def __init__(self):
        self._record = [] # format [[line, col, error text], [line, col, error text]]
        self._lenRecord = 1
        self.setRecord(0, 0, "Example Error") # [Temp]

    def getRecord(self):
        return self._record

    def setRecord(self, line, col, error):
        """
        Tuple appended to self Record
        """
        self._record.append([line, col, error])
        self._lenRecord += 1

    def displayRecord(self):
        """
        Outputs line, col, and error from each Tuple stored in self Record
        """
        for line, col, error in self._record:
            print(f"{line}, {col}, {error}, error detected")

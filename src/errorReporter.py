class Reporter:

    def __init__(self):
        self.record = [] # format [[line, col, error text], [line, col, error text]]

    def setRecord(self, line, col, error):
        # Error Tuple appended to self._record
        
        self.record.append([line, col, error])

    def insertDefaultError(self, line, col, error):
        # Insert Error Tuple at index 0 of self._record.
        # Used by errors that fail by default.

        self.record.insert(0, [line, col, error])

    def removeDefaultError(self):
        # Removes Error Tuple at index 0 of self._record.
        # Used by errors that fail by default.

        del self.record[0]

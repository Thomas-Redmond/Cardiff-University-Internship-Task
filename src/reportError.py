class Reporter:

    def __init__(self):
        self._record = [] # format [[line, col, error text], [line, col, error text]]

    def setRecord(self, line, col, error):
        """
        Error Tuple appended to self._record
        """
        self._record.append([line, col, error])

    def insertDefaultError(self, line, col, error):
        """
        Insert Error Tuple at index 0 of self._record.
        Used by errors that fail by default.
        """
        self._record.insert(0, [line, col, error])

    def removeDefaultError(self):
        """
        Removes Error Tuple at index 0 of self._record.
        Used by errors that fail by default.
        """
        del self._record[0]

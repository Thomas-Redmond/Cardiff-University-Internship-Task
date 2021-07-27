class Reporter:

    def __init__(self):
        Record = [] # format [line, col, error text]

    def getRecord(self):
        return Record

    def setRecord(self, line, col, error):
        Record.append(line, col, error)

    def displayRecord(self):
        for line, col, error in Record:
            print(f"{line}, {col}, {error}, error detected")

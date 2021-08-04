class PluginError:

    def __init__(self, reportHere):
        self._reportHere = reportHere

    def run(self):
        # Overridden by Child class
        return

    def success(self):
        """
        [Temp] Informs user of success
        """
        print(f"{self._Code} Success")
        return

    def fail(self):
        """
        Appends details of failed test to Record in class Reporter
        [Temp] Notifies user of failure
        """
        self._reportHere.setRecord(0, 0, self._Code + ": " + self._Text)
        print(f"{self._Code} Failed")
        return

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        return

    def setType(self, Type):
        self._Type = Type
        return

    def getType(self):
        return self._Type

    def setCode(self, Code):
        self._Code = Code
        return

    def getCode(self):
        return self._Code

    def setText(self, Text):
        self._Text = Text
        return

    def getText(self):
        return self._Text

class PluginError:
    self._Type = None
    self._Code = None
    self._Text = ""

    def __init__(self, Type, Code, Text, reportHere):
        # Pass Type of error, error code, and descriptive text as parameters
        self._Type = Type
        self._Code = Code
        self._Text = Text
        self._reportHere = reportHere


    def run(self):
        # Overridden by Child class
        return

    def success(self):
        return

    def fail(self):

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

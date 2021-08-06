import os
import sys
filename = sys.argv[1]
if os.path.exists(filename):
    pass
else:
    raise ModuleNotFoundError
address = filename[0 : filename.rfind("\\")]
sys.path.insert(0, address)
Squash = __import__(filename[-9 :-3])

class PluginError:

    def __init__(self, reportHere):
        self._reportHere = reportHere
        self._Loc = [0, 0]

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
        self._reportHere.setRecord(self._Loc[0], self._Loc[1], self._Code + ": " + self._Text)
        print(f"{self._Code} Failed")
        return

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        print(f'Loc: {self._Loc[0], self._Loc[1]}')
        return

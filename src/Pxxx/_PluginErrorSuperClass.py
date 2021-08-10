import sys
from pathlib import Path

def importModule(filename):
    # Tests if filename parameter exists given complete address
    # Raises ModuleNotFoundError otherwise
    # Adds parent directory to path and returns filename stem
    if Path.exists(filename):
        sys.path.insert(0, str(filename.parent))
        return filename.stem
    else:
        raise ModuleNotFoundError(f"Address {filename} was not found")

filename = Path(sys.argv[1])
Squash = __import__(importModule(filename))


class PluginError:

    def __init__(self, reportHere):
        self._reportHere = reportHere
        self._Loc = [0, 0]

    def run(self): pass
        # Overridden by Child class

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

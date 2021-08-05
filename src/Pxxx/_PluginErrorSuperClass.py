import sys
import os
import importlib.util


def importUserFile():
    """
    Imports Squash.py using parameter given in flake8 run command
    Presumes format: flake8 E:/doc/.../Squash.py
    Isolates filename and address.
    Adds address to path and imports filename
    """
    try:
        filename = sys.argv[1]
        if os.path.exists(filename):
            index = filename.rfind("/")
            address = filename[0 : index ]
            filename = filename[index + 1 : ]

        else:
            raise ModuleNotFoundError
        spec = importlib.util.spec_from_file_location(filename, address)
        Squash = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(Squash)
        return
    except Exception as e:
        print(e)

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

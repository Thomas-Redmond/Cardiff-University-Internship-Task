"""
P720: Must use the csv module
"""
import sys
import os

filename = sys.argv[1]
if ".py" in filename:
    filename = filename[0:-3]
address = os.getcwd()
sys.path.append(address)
Squash = __import__(filename)

from _PluginErrorSuperClass import PluginError

class P720(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P720"
        self._Text = "Must use the csv module"

    def run(self):
        """
        Checks that csv module has been imported
        """

        try:
            if "csv" not in sys.modules:
                self.fail()
            else:
                self.success()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

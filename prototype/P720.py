"""
P720: Must use the csv module
"""
import sys
import Squash
from _PluginErrorSuperClass import PluginError

class P720(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P720"
        self._Text = "Must use the csv module"

    def run(self):

        try:
            if "csv" not in sys.modules:
                self.fail()
            else:
                self.success()
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")

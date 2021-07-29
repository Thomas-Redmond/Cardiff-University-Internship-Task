"""
Checks each data item is a number
"""

import Squash
from _PluginErrorSuperClass import PluginError

class P711(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P711"
        self._Text = "Each item in the Tuple should be a number"

    def run(self, filename):
        try:
            desired_col_num = 10

            data = Squash.readCSV(filename)
            for row in data:
                for item in row:
                    if item.isType("Float") or item.isType("Integer"):
                        # skip
                    else:
                        self.fail()
                        return
            self.success()
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")

        return

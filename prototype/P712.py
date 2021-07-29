"""
Checks dimensions of returned matrix has handled bad column
"""

import Squash
from _PluginErrorSuperClass import PluginError

class P712(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P712"
        self._Text = "Checks dimension of returned matrix to see if desired size"

    def run(self, filename):
        try:
            desired_col_num = 10

            data = Squash.readCSV(filename)
            for row in data:
                if len(row) != desired_col_num:
                    self.fail()
                    return
            self.success()
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")

        return

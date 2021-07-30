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

    def run(self):
        try:
            desired_col_num = 3

            data = Squash.readCSV("data.csv")
            for row in data:
                if len(row) != desired_col_num:
                    self.fail()
                    return
            self.success()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

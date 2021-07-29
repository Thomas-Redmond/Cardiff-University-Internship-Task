"""
Checks dimensions of returned matrix has skipped first row
"""

import Squash
from _PluginErrorSuperClass import PluginError

class P710(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P710"
        self._Text = "Number of Rows read from csv is incorrect"

    def run(self, filename):
        try:
            desired_row_num = 10

            data = Squash.readCSV(filename)
            if len(data) == desired_row_num:
                self.success()
            else:
                self.fail()
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")

        return

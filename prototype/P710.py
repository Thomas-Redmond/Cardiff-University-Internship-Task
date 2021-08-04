"""
Checks dimensions of returned matrix has skipped first row
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

class P710(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P710"
        self._Text = "Number of Rows read from csv is incorrect"

    def run(self):
        """
        Checks the output of Squash.readCSV has the correct number of rows
        """
        try:
            desired_row_num = 2

            data = Squash.readCSV("data.csv")
            if len(data) == desired_row_num:
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

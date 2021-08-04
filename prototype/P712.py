"""
Checks dimensions of returned matrix has handled bad column
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

class P712(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P712"
        self._Text = "Checks dimension of returned matrix to see if desired size"

    def run(self):
        """
        Checks that every row has the desired number of columns
        """
        try:
            desired_col_num = 2 # Modify to fit required function

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

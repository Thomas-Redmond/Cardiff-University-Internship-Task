from pathlib import Path

from src.Pxxx._PluginErrorSuperClass import Squash
from src.Pxxx._PluginErrorSuperClass import filename
from src.Pxxx._PluginErrorSuperClass import PluginError

class P712(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P712"
        self._Text = "The number of columns in the returned matrix is incorrect"

    def run(self):
        """
        Checks that every row has the desired number of columns
        """
        try:
            desired_col_num = 2 # Modify to fit required function

            data = Squash.readCSV("test.csv")
            for row in data:
                if len(row) != desired_col_num:
                    self.fail()
                    return
            self.success()

        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

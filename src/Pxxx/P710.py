from pathlib import Path

from src.Pxxx._PluginErrorSuperClass import Squash
from src.Pxxx._PluginErrorSuperClass import filename
from src.Pxxx._PluginErrorSuperClass import PluginError

class P710(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P710"
        self._Text = "Number of Rows read from csv is incorrect"

    def run(self):
        """
        Checks the output of Squash.readCSV has the correct number of rows
        """
        address = Path(filename)
        address = address.with_name('data.csv')
        try:
            desired_row_num = 5
            if Path.exists(address):
                data = Squash.readCSV(address)
                if len(data) == desired_row_num:
                    self.success()
                else:
                    self.fail()
            else:
                raise FileNotFoundError(f"data.csv not found in directory {address}")

        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

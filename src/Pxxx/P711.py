from pathlib import Path

from src.Pxxx._PluginErrorSuperClass import Squash
from src.Pxxx._PluginErrorSuperClass import filename
from src.Pxxx._PluginErrorSuperClass import PluginError

class P711(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P711"
        self._Text = "Each item returned in the Tuple should be a number"

    def run(self):
        """
        Checks that each item returned by Squash.readCSV is a number
        """
        try:

            data = Squash.readCSV("test.csv")
            for row in data:
                for item in row:
                    if isinstance(item, (int, float, complex)):
                        pass
                    else:
                        self.fail()
                        return
                self.success()

        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

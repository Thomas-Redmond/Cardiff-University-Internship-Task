"""
Checks each data item is a number
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

class P711(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P711"
        self._Text = "Each item in the Tuple should be a number"

    def run(self):
        """
        Checks that each item returned by Squash.readCSV is a number
        """
        try:
            data = Squash.readCSV("data.csv")
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

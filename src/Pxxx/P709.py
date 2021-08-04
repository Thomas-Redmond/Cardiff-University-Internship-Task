"""

"""

import sys
import os
filename = sys.argv[1]
if ".py" in filename:
    filename = filename[0:-3]
address = os.getcwd()
if filename[0:1] == "./":
    filename = filename[2:]
if "/" in filename:
    index = filename.rfind("/")
    address = address + filename[0:index]
    filename = filename[index + 1: ]
sys.path.append(address)
Squash = __import__(filename)

from _PluginErrorSuperClass import PluginError

class P709(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P709"
        self._Text = "Question asked for a different function name"

    def run(self):
        """
        Checks that the function game exists
        """
        try:
            if "game" in dir(Squash):
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

"""
No rounding inside the function
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

class P704(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P704"
        self._Text = "Do not round inside the function"

    def run(self):
        """
        Tests that winProbability returns a unrounded value
        Checks ten times using various parameters.
        If float found then success
        """
        # Runs 10 times, checking against a vareity of parameters
        # fails test if no Float values are found in all ten attempts
        try:
            for i in range(10):
                if (type(Squash.winProbability(i, 1)) == "float"):
                    self.success()
                    i = 11
                elif (type(Squash.winProbability(i, 1)) != "float") and i == 10:
                    self.fail()
                else:
                    # loop back round
                    pass
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

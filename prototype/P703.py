"""
winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail
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

class P703(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P703"
        self._Text = "winProbability must return a number"


    def run(self):
        # Function Override
        """
        Tests that winProbability returns an integer, float or complex value
        """
        try:
            variableReturned = Squash.winProbability(2, 1)
            if isinstance(variableReturned, (int, float, complex)):
                self.success()
            else:
                self.fail()

        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

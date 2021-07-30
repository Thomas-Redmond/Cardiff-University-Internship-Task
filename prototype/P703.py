"""
winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail
"""
import Squash
from _PluginErrorSuperClass import PluginError

class P703(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P703"
        self._Text = "winProbability must return a number"


    def run(self):
        # Function Override
        variableReturned = Squash.winProbability(2, 1)
        if isinstance(variableReturned, float) or isinstance(variableReturned, int):
            self.success()
        else:
            self.fail()

        #except:
            #print(f"{self._Code} Test Aborted due to unexpected error")

        return

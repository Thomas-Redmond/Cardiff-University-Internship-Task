"""
No rounding inside the function
"""
import Squash
from _PluginErrorSuperClass import PluginError

class P704(PluginError):

    def __init__(self, reportHere):
        super.__init__(reportHere)
        self._Code = "P704"
        self._Text = "Do not round inside the function"

    def run(self):
        # Runs 10 times, checking against a vareity of parameters
        # fails test if no Float values are found in all ten attempts
        try:
            for i in range(10):
                if (Squash.winProbability(i, 1).isType("Float")):
                    self.success()
                    i = 11
                elif not Squash.winProbability(i, 1).isType("Float") and i == 10:
                    self.fail()
                else:
                    # loop back round
                    pass
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")
        return

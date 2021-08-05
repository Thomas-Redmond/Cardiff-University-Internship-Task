import src.Pxxx._PluginErrorSuperClass as PESC

import os
import sys
filename = sys.argv[1]
if os.path.exists(filename):
    pass
else:
    raise ModuleNotFoundError
address = filename[0 : filename.rfind("\\")]
sys.path.insert(0, address)
Squash = __import__(filename[-9 :-3])

class P703(PESC.PluginError):

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

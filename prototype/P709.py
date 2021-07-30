"""

"""

import Squash
from _PluginErrorSuperClass import PluginError

class P709(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P709"
        self._Text = "Question asked for a different function name"

    def run(self):
        try:
            if "game" in dir(Squash):
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

"""
Don't use Global
"""
import Squash
from _PluginErrorSuperClass import PluginError

class P719(PluginError):

    def __init__(self, reportHere):
        super.__init__(reportHere)
        self._Code = "P719"
        self._Text = "Do not use Global variables"

    def run(self):
        try:
            if len(Squash.is_global) == 0:
                self.fail()
            else:
                self.success()
        except:
            print(f"{self._Code} Test Aborted due to unexpected error")
        return

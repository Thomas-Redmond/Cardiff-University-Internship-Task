from _PluginErrorSuperClass import PluginError

import sys
import os

filename = sys.argv[1]
if ".py" in filename:
    filename = filename[0:-3]
address = os.getcwd()
sys.path.append(address)
Squash = __import__(filename)

class P705(PluginError):

    def __init__(self, reportHere):
        super.__init__(reportHere)
        self._Code = "P705"
        self._Text = "Do not hardcode filename, pass as an argument"

    def run(self):
        try:
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

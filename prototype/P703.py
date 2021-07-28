"""
winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail
"""

class P703(PluginError):

    def __init__(self, reportHere):
        super.__init__(reportHere)
        self._Code = "P703"
        self._Text = "winProbability must return a number"


    def run(self):
    # Function Override
    try:
        variableReturned = Squash.winProbability()
        if variableReturned.type() == "float" or variableReturned.type() == "int":
            self.success()
        else:
            self.fail()

    except:
        print(f"{self._Code} Test Aborted due to unexpected error")

    return

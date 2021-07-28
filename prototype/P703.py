"""
winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail
"""

class P703(PluginError):

    def __init__(self, Type, Code, Text, reportHere):
        super.__init__(Type, Code, Text, reportHere)
        self._Type = "Plugin Error"
        self._Code = 703
        self._Text = "winProbability must return a number"


    def run():
    # Function Override
    try:
        variableReturned = Squash.winProbability()
        if variableReturned.type() == "float" or variableReturned.type() == "int":
            self.success()
        else:
            self.fail()

    except:
        print("Unexpected Error. Test Aborted")

    return

"""
winProbability function must return number.
Positive result if Float / Integer returned.
Default = Fail
"""

class P703(PluginError):

    def __init__(self, Type, Code, Text, reportHere):
        super.__init__(Type, Code, Text, reportHere)

    def run():
    # Function Override
    try:
        variableReturned = Squash.winProbability()
        if variableReturned.type() == "float" or variableReturned.type() == "int":
            print("Success")
        else:
            print("Test Failed")

    except:
        print("Unexpected Error")

    return

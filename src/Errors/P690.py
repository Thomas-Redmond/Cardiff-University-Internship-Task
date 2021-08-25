from Errors.errorType import basicError

class P690(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P690"
        self.errorText = "Recommended Function names not detected. See README.md for details"

    def run(self, Squash):
        """
        Tests that function names used in other tests are available
        """
        try:
            listOfFuncs = [
            "englishgame",
            "game",
            "q1a",
            "readCSV",
            "plotWinProbabilities",
            "winProbability"

            ]
            for funcName in listOfFuncs:
                if funcName not in dir(Squash):
                    self.fail()
                    return

        except Exception as e:
            print(e)
            self.fail()

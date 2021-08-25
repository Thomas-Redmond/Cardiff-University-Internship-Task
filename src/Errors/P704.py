from Errors.errorType import basicError

class P704(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P704"
        self.errorText = "Do not round inside the function"

    def run(self, Squash):
        """
        Tests that winProbability returns a unrounded value
        Checks ten times using various parameters.
        If float found then success
        """
        # Runs 10 times, checking against a vareity of parameters
        # fails test if no Float values are found in all ten attempts
        try:
            for i in range(10):
                if (type(Squash.winProbability(i, 1)) == "float"):
                    self.success()
                    i = 11
                elif (type(Squash.winProbability(i, 1)) != "float") and i == 10:
                    self.fail()
                else:
                    # loop back round
                    pass
        except Exception as e:
            print(e)
            self.fail()

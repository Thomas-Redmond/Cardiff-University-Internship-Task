from src.Errors.errorType import basicError

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
        # fails test if no remainder found in at least one int(result) - result
        try:
            for i in range(10):
                returnedValue = Squash.winProbability(i, 1)
                if (returnedValue - int(returnedValue) > 0):
                    self.success()
                    i = 11
                elif (returnedValue - int(returnedValue) <= 0) and (i == 10):
                    self.fail()
                else:
                    # loop back round
                    pass
        except Exception as e:
            print(e)
            self.fail()

from Errors.errorType import basicError

class P709(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P709"
        self._errorText = "Function game is missing"


    def run(self):
        """
        Checks that the function game exists
        """
        try:
            if "game" in dir(Squash):
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(e)
            self.fail()

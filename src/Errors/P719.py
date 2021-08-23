from Errors.errorType import basicError

class P719(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P719"
        self._errorText = "Do not use Global variables"

    def run(self):
        """
        Tests for global variables in Squash [Code broken]
        """
        try:
            if len(Squash.is_global) == 0:
                self.fail()
            else:
                self.success()
        except Exception as e:
            print(e)
            self.fail()

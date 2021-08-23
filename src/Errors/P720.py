import sys
from Errors.errorType import basicError

class P720(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P720"
        self._errorText = "Must use the csv module"

    def run(self):
        """
        Checks that csv module has been imported
        """

        try:
            if "csv" not in sys.modules:
                self.fail()
            else:
                self.success()
        except Exception as e:
            print(e)
            self.fail()

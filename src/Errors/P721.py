import sys
from src.Errors.errorType import basicError

class P721(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P721"
        self.errorText = "Must use the matplotlib module"

    def run(self, Squash):
        """
        Checks that matplotlib module has been imported
        """

        try:
            if "matplotlib" not in sys.modules:
                self.fail()
            else:
                self.success()
        except Exception as e:
            print(e)
            self.fail()

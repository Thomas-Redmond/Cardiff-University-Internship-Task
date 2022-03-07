from pathlib import Path
from src.Errors.errorType import basicError

class RP01u12(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "RP01u12"
        self.errorText = "Returns -1 on input of '1'"

    def run(self, TestThisFile):
        """
        Tests input of parameter 1 (type string)
        """
        try:
            result = TestThisFile.program('1')
            if result != -1:
                self.success()
                return
            else:
                self.fail()
                return

        except Exception as e:
            print(e)
            self.fail()

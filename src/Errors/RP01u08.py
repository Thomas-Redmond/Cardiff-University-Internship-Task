from pathlib import Path
from src.Errors.errorType import basicError

class RP01u08(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "RP01u08"
        self.errorText = "Check Output is type list given GOOD input"
        #self.testData = Path("src/Errors/testData/test.csv")

    def run(self, TestThisFile):
        """
        Tests input parameter '9J4B72q' to function "program" returns type list
        """
        try:
            result = TestThisFile.program('9J4B72q')
            if isinstance(result, list):
                self.success()
                return
            else:
                self.fail()
                return

        except Exception as e:
            print(e)
            self.fail()

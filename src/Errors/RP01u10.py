from pathlib import Path
from src.Errors.errorType import basicError

class RP01u10(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "RP01u10"
        self.errorText = "Check Output is -1 given bad input"
        #self.testData = Path("src/Errors/testData/test.csv")

    def run(self, TestThisFile):
        """
        Tests input parameter [] to function "program" returns -1
        """
        try:
            result = TestThisFile.program([])
            if result == -1:
                self.success()
                return
            else:
                self.fail()
                return

        except Exception as e:
            print(e)
            self.fail()

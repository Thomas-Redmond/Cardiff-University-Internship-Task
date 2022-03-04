from pathlib import Path
from src.Errors.errorType import basicError

class Test(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "U003"
        self.errorText = "Check Output is type int given bad input"
        #self.testData = Path("src/Errors/testData/test.csv")

    def run(self, TestThisFile):
        """
        Tests input parameter [] to function "program" returns type int
        """
        try:
            result = TestThisFile.program([])
            if isinstance(result, int):
                self.success()
                return
            else:
                self.fail()
                return

        except Exception as e:
            print(e)
            self.fail()

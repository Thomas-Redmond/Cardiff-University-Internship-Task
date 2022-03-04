from pathlib import Path
from src.Errors.errorType import basicError

class Test(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "U100"
        self.errorText = "Test 2 dimensional list GOOD input [['9J4B72q']] expect [9, 4, 7, 2]"
        #self.testData = Path("src/Errors/testData/test.csv")

    def run(self, TestThisFile):
        """
        Test 2 dimensional list GOOD input [["9J4B72q"]] expect [9, 4, 7, 2]
        """
        try:
            result = TestThisFile.program([['9J4B72q']])
            if result == [9, 4, 7, 2]:
                self.success()
                return
            else:
                self.fail()
                return

        except Exception as e:
            print(e)
            self.fail()

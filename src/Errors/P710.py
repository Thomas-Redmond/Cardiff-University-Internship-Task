from pathlib import Path
from Errors.errorType import basicError
import sys
class P710(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P710"
        self._errorText = "Number of Rows read from csv is incorrect"
        self._testData = Path("src/Errors/testData/test.csv")

    def run(self, Squash):
        """
        Checks the output of Squash.readCSV has the correct number of rows
        """

        try:
            desired_row_num = 5
            data = Squash.readCSV(self._testData)
            if len(data) == desired_row_num:
                self.success()
            else:
                self.fail()

        except Exception as e:
            print(e)
            self.fail()
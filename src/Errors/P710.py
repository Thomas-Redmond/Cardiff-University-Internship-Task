from pathlib import Path
from src.Errors.errorType import basicError
import sys
class P710(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P710"
        self.errorText = "Number of Rows read from csv is incorrect"
        self.testData = Path("src/Errors/testData/test.csv")

    def run(self, Squash):
        """
        Checks the output of Squash.readCSV has the correct number of rows
        """

        try:
            desired_row_num = 5
            data = Squash.readCSV(self.testData)
            if len(data) == desired_row_num:
                self.success()
            else:
                self.fail()

        except Exception as e:
            print(e)
            self.fail()

from pathlib import Path
from Errors.errorType import basicError

class P712(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P712"
        self._errorText = "The number of columns in the returned matrix is incorrect"
        self._testData = Path("src/Errors/testData/test.csv")

    def run(self, Squash):
        """
        Checks that every row has the desired number of columns
        """
        try:
            desired_col_num = 2 # Modify to fit required function

            data = Squash.readCSV(self._testData)
            for row in data:
                if len(row) != desired_col_num:
                    self.fail()
                    return
            self.success()

        except Exception as e:
            print(e)
            self.fail()

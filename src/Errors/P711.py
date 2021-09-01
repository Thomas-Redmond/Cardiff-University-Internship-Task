from pathlib import Path
from src.Errors.errorType import basicError

class P711(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P711"
        self.errorText = "Each item returned in the Tuple should be a number"
        self.testData = Path("src/Errors/testData/test.csv")

    def run(self, Squash):
        """
        Checks that each item returned by Squash.readCSV is a number
        """
        try:

            data = Squash.readCSV(self.testData)
            for row in data:
                for item in row:
                    if isinstance(item, (int, float, complex)):
                        pass
                    else:
                        self.fail()
                        return
            self.success()

        except Exception as e:
            print(e)
            self.fail()

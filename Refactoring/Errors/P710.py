from errorType import basicError

class P710(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P710"
        self._errorText = "Number of Rows read from csv is incorrect"

    def run(self):
        """
        Checks the output of Squash.readCSV has the correct number of rows
        """

        try:
            desired_row_num = 5
            data = Squash.readCSV("test.csv")
            if len(data) == desired_row_num:
                self.success()
            else:
                self.fail()

        except Exception as e:
            print(e)
            self.fail()

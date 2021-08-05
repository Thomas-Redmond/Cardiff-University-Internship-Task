import src.Pxxx._PluginErrorSuperClass as PESC

class P709(PESC.PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P709"
        self._Text = "Question asked for a different function name"

    def run(self):
        """
        Checks that the function game exists
        """
        try:
            if "game" in dir(Squash):
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

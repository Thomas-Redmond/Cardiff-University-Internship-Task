import src.Pxxx._PluginErrorSuperClass as PESC

class P705(PESC.PluginError):

    def __init__(self, reportHere):
        super.__init__(reportHere)
        self._Code = "P705"
        self._Text = "Do not hardcode filename, pass as an argument"

    def run(self):
        try:
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()

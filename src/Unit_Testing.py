from .Pxxx.P703 import P703 as P703_Test
from .Pxxx.P704 import P704 as P704_Test
from .Pxxx.P709 import P709 as P709_Test
from .Pxxx.P710 import P710 as P710_Test
from .Pxxx.P711 import P711 as P711_Test
from .Pxxx.P712 import P712 as P712_Test
#from .Pxxx.P719 import P719 as P719_Test
from .Pxxx.P720 import P720 as P720_Test

class Controller:

    def __init__(self, errorReporter):
        # pass Error_Reporter instance by reference
        # allows this class to utilise its functions
        self._reportHere = errorReporter
        self._testsToRun = [
            P703_Test, P704_Test, P709_Test, P710_Test, P711_Test, P712_Test, P720_Test]

    def run(self):
        """
        For every test in self._testsToRun create an instance and run that test.
        Errors will be recorded in the instance of Reporter passed to this class upon instantiation.
        """
        for test in self._testsToRun:
            try:
                instance = test(self._reportHere)
                instance.run()
            except Exception as e:
                print(f"Unexpected Error {e}")
        return

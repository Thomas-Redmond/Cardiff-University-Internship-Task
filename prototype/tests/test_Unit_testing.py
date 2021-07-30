import Unit_Testing
import reportError

def test_init():
    r = reportError.Reporter()
    u = Unit_Testing.Controller(r)
    assert u._reportHere == r

import Unit_Testing
import reportError

def test_init():
    r = reportError.Reporter()
    u = Unit_Testing.Controller(r)
    assert u._reportHere == r

def test_run_method():
    r = reportError.Reporter()
    u = Unit_Testing.Controller(r)
    u.run()
    assert r.getRecord() == 0

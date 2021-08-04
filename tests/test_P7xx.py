import reportError
from P710 import P710

def test_fail():
    r = reportError.Reporter()
    failTest = P710(r)
    failTest.fail()
    assert r.getRecord() == [[0, 0, "P710: Number of Rows read from csv is incorrect"]]

def test_success():
    r = reportError.Reporter()
    successTest = P710(r)
    successTest.success()
    assert r.getRecord() == []

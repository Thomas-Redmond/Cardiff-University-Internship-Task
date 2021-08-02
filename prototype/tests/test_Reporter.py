import reportError

def test_init():
    # Tests whether Reporter Class when initiated has only empty record
    r = reportError.Reporter()
    assert r.getRecord() == []

def test_setRecord():
    r = reportError.Reporter()
    r.setRecord("line", "col", "errorText")
    assert r.getRecord() == [["line", "col", "errorText"]]

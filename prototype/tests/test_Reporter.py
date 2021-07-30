import reportError

def test_init():
    # Tests whether Reporter Class when initiated has only empty record
    r = reportError.Reporter()
    assert r.getRecord() == []

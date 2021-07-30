import reportError

def test_trivial_case():
    # Tests whether Reporter Class when initiated has only empty record
    r = reportError.Reporter()
    assert r.getRecord() == []

def 

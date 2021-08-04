
import Unit_Testing
import reportError
import Squash
from P703 import P703 as P703_Test
from P704 import P704 as P704_Test
from P709 import P709 as P709_Test
from P710 import P710 as P710_Test
from P711 import P711 as P711_Test
from P712 import P712 as P712_Test
from P719 import P719 as P719_Test
from P720 import P720 as P720_Test


def test_init():
    r = reportError.Reporter()
    u = Unit_Testing.Controller(r)
    assert u._reportHere == r

def test_P703():
    r = reportError.Reporter()
    test = P703_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P704():
    r = reportError.Reporter()
    test = P704_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P709():
    r = reportError.Reporter()
    test = P709_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P710():
    r = reportError.Reporter()
    test = P710_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P711():
    r = reportError.Reporter()
    test = P711_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P712():
    r = reportError.Reporter()
    test = P712_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P719():
    r = reportError.Reporter()
    test = P719_Test(r)
    test.run()
    assert r.getRecord() == []

def test_P720():
    r = reportError.Reporter()
    test = P720_Test(r)
    test.run()
    assert r.getRecord() == []

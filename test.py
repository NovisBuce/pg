from aplikace import soucet, fibonachi
from zkouska1 import pozpatku, pozpatku_1
from zkouska2 import operace

def test_soucet_2():
    assert soucet(1, 1) == 2

def test_soucet_3():
    assert soucet(1, 2) == 3

def test_fibonachi_5():
    assert fibonachi(5) == [1, 1, 2, 3, 5]

def test_fibonachi_10():
    assert fibonachi(10) == [1, 1, 2, 3, 5, 8]

def test_pozpatku():
    assert pozpatku("ahoj") == "joha"
    assert pozpatku("ahoj, jak se mas?") == "?sam es kaj ,joha"

def test_pozpatku_2():
    assert pozpatku_1("ahoj") == "joha"
    assert pozpatku_1("ahoj, jak se mas?") == "?sam es kaj ,joha"

def test_operace():
    assert operace("+", 1, 2) == 3
    assert operace("-", 2, 1) == 1
    assert operace("*", 0, 5) == 0
    assert operace("/", 4, 2) == 2
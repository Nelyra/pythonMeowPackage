from meow_package.banque import meow

def test_meow():
    assert meow(250, 30) == 300
    assert meow(150, 30) == 180
from codecs import ascii_encode
from bank import value


def test_bank():

    def hello():
        assert value("hello") == 0
        assert value("Hello") == 0
        assert value("HELLO") == 0

    def h():
        assert value("h") == 20
        assert value("H") == 20

    def _():
        assert value("Testing") == 100

from twttr import shorten


def test_shorten():
    assert shorten("alin") == "ln"
    assert shorten("Alin") == "ln"
    assert shorten("cs50") == "cs50"
    assert shorten("ALIN") == "LN"
        
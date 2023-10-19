from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("cs50-python") == "cs50-pthn"
    assert shorten ("UPPERCASE") == "PPRCS"
    

main()
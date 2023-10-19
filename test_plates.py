from plates import is_valid


def test_plates():
    assert is_valid("cs00") == False
    assert is_valid("Cs50a") == False
    assert is_valid("CSS05") == False
    assert is_valid("CSSS") == True
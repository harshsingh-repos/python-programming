import pytest
from programs.findingChOccurrences import countOccurreces

textString = "This is a test"
numString = "12343212345677265"

def test_countOccurrecesString():
    """
    Test to count the Occurrences of the characters in the given string
    """
    countOccurrence = countOccurreces(textString)
    assert countOccurrence["t"] == 3
    assert countOccurrence["i"] == 2

def test_countOccurrecesNumber():
    """
    Test to count the Occurrences of the characters in the given string
    """
    countOccurrence = countOccurreces(numString)
    assert countOccurrence["1"] == 2
    assert countOccurrence["2"] == 4

if __name__ == "__main__":
    pytest.main()
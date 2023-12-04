import pytest
from .cards.api import Card

def test_with_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    if c1 != c2:
        pytest.fail("they don't match")




# if __name__ == '__main__':
#     test_with_fail()
from cards.api import Card

def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken") 
    print(c1.id, c1.owner, c1.state, c1.summary)
    assert c1 == c2



if __name__ == '__main__':
    test_equality_fail()
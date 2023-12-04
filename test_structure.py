from .cards.api import Card

def test_to_dict():
    # GIVEN a Card object with known contents 
    c1 = Card("someting", "brian", "todo", 123)

    # WHEN we call to_dict() on the object
    c2 = c1.to_dict()

    # THEN the result will be a dictionary with know content
    c2_expected = {
        "summary": "something", 
        "owner": "brian", 
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected




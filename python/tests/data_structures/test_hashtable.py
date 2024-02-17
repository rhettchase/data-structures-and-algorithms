import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_hash_key():
    hashtable = Hashtable()
    actual = hashtable._hash("Cat")
    assert 0 <= actual < hashtable._size

def test_hash_twice():
    hashtable = Hashtable()
    first = hashtable._hash("Cat")
    second = hashtable._hash("Cat")
    assert first == second

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_insert_twice():
    hashtable = Hashtable()
    hashtable.set("cat", "climbs on trees")
    hashtable.set("cat", "plays with yarn")
    actual = hashtable.get("cat")
    expected = "plays with yarn"
    assert actual == expected

def test_key_not_exist():
    hashtable = Hashtable()
    actual = hashtable.get("non existing key")
    expected = None
    assert actual == expected

def test_key_not_exist_again():
    """
    NOTE: demands that dog and god hash act the same
    """
    hashtable = Hashtable()
    hashtable.set("dog", "bark")
    actual = hashtable.get("god")
    expected = None
    assert actual == expected

def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("strawberry", "berry fruit")
    actual = hashtable.keys()
    expected = ["apple", "strawberry"]
    assert sorted(actual) == sorted(expected)

def test_repeat_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "For apple pie")
    hashtable.set("strawberry", "berry fruit")
    actual = hashtable.keys()
    expected = ["apple", "strawberry"]
    assert sorted(actual) == sorted(expected)


def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("strawberry", "berry fruit")
    assert hashtable.has("apple")
    assert hashtable.has("strawberry")
    assert not hashtable.has("cheetos")

def test_has_collision():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "A gift for the teacher")
    actual = hashtable.get("apple")
    expected = "A gift for the teacher"
    assert actual == expected



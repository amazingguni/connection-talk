from item import Item

def test_get_name():
    item = Item("name_123")
    assert item.get_name() == "name_123"

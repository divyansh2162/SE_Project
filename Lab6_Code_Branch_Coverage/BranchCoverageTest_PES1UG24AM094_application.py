
import pytest
from vending_machine import select_item, make_change, purchase


# SELECT ITEM TESTS

def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_item_missing_from_stock():
    assert select_item("cola", {}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_valid_selection():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# MAKE CHANGE TESTS

def test_no_change_needed():
    assert make_change(0) == []


def test_exact_coin():
    assert make_change(100) == [100]


def test_multiple_coins():
    assert make_change(185) == [100, 50, 25, 10]


def test_impossible_change():
    assert make_change(3) is None


def test_negative_amount():
    with pytest.raises(ValueError):
        make_change(-1)


# PURCHASE TESTS

def test_purchase_invalid_item():
    assert purchase("water", {}, 200) == ("invalid", [])


def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


def test_purchase_insufficient_credit():
    assert purchase("cola", {"cola": 2}, 100) == ("insufficient", [])


def test_purchase_no_exact_change():
    stock = {"cola": 2}
    assert purchase("cola", stock, 153) == ("no_exact_change", [])
    assert stock["cola"] == 2


def test_successful_purchase():
    stock = {"cola": 2}
    result = purchase("cola", stock, 200)

    assert result == ("dispensed", [50])
    assert stock["cola"] == 1


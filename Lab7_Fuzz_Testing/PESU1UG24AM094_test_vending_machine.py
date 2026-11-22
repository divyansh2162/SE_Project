
from hypothesis import given, strategies as st

from vending_machine import parse_coins, slot_position, change_due


@given(st.one_of(st.text(), st.none()))
def test_parse_coins_no_crash(value):
    result = parse_coins(value)

    assert result is None or (
        isinstance(result, list)
        and all(isinstance(coin, int) and coin > 0 for coin in result)
    )


@given(st.one_of(st.text(), st.none()))
def test_slot_position_no_crash(value):
    result = slot_position(value)

    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and 0 <= result[0] <= 25
        and result[1] >= 0
    )


@given(st.one_of(st.text(), st.none()))
def test_change_due_no_crash(value):
    result = change_due(value)

    assert result is None or (
        isinstance(result, str) and result.endswith(" five-coins")
    )


# Valid input tests

def test_parse_valid_coins():
    assert parse_coins("5,10,25") == [5, 10, 25]


def test_valid_slot_position():
    assert slot_position("B7") == (1, 6)


def test_valid_change_due():
    assert change_due("200/150") == "10 five-coins"


# Invalid input tests

def test_empty_coin_input():
    assert parse_coins("") is None


def test_invalid_slot_input():
    assert slot_position("") is None


def test_invalid_payment_input():
    assert change_due("invalid") is None


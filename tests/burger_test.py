from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from tests.helpers import _make_ingredient_mock


def test_set_buns_assigns_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)

    assert burger.bun is mock_bun


def test_add_ingredient_appends(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    ing = _make_ingredient_mock("SAUCE", "ketchup", 10)
    burger.add_ingredient(ing)

    assert burger.ingredients == [ing]


@pytest.mark.parametrize(
    "index,expected_names",
    [
        (0, ["b"]),
        (1, ["a"]),
    ],
)
def test_remove_ingredient(mock_bun, index, expected_names):
    burger = Burger()
    burger.set_buns(mock_bun)
    a = _make_ingredient_mock("FILLING", "a", 1)
    b = _make_ingredient_mock("FILLING", "b", 2)
    burger.add_ingredient(a)
    burger.add_ingredient(b)
    burger.remove_ingredient(index)

    assert [i.get_name() for i in burger.ingredients] == expected_names


@pytest.mark.parametrize(
    "old_index,new_index,expected_order",
    [
        (0, 1, ["b", "a", "c"]),
        (2, 0, ["c", "a", "b"]),
        (1, 0, ["b", "a", "c"]),
    ],
)
def test_move_ingredient(mock_bun, old_index, new_index, expected_order):
    burger = Burger()
    burger.set_buns(mock_bun)
    for letter, price in [("a", 1), ("b", 2), ("c", 3)]:
        burger.add_ingredient(_make_ingredient_mock("SAUCE", letter, float(price)))
    burger.move_ingredient(old_index, new_index)

    assert [i.get_name() for i in burger.ingredients] == expected_order


def test_get_price_returns_sum_of_bun_and_ingredients(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    sauce = _make_ingredient_mock("SAUCE", "s1", 10)
    filling = _make_ingredient_mock("FILLING", "f1", 5.5)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    expected_price = (
        mock_bun.get_price.return_value * 2
        + sauce.get_price.return_value
        + filling.get_price.return_value
    )

    assert burger.get_price() == expected_price


def test_get_receipt_returns_formatted_string(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    ing = _make_ingredient_mock("SAUCE", "Mayo", 20)
    burger.add_ingredient(ing)
    receipt_price = 999.0
    burger.get_price = Mock(return_value=receipt_price)
    receipt = burger.get_receipt()

    expected = (
        f"(==== {mock_bun.get_name.return_value} ====)\n"
        f"= {ing.get_type.return_value.lower()} {ing.get_name.return_value} =\n"
        f"(==== {mock_bun.get_name.return_value} ====)\n"
        "\n"
        f"Price: {receipt_price}"
    )

    assert receipt == expected

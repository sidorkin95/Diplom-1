# Юнит-тесты класса Burger

from unittest.mock import Mock, patch

import pytest

from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    # Мок булки: фиксированные имя и цена для get_price и текста чека.
    bun = Mock()
    bun.get_name.return_value = "Sesame"
    bun.get_price.return_value = 50.0
    return bun


def _make_ingredient_mock(ing_type: str, name: str, price: float):
    m = Mock()
    m.get_type.return_value = ing_type
    m.get_name.return_value = name
    m.get_price.return_value = price
    return m


def test_set_buns_assigns_bun(mock_bun):
    # set_buns сохраняет переданную булку в атрибуте bun
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun is mock_bun


def test_add_ingredient_appends(mock_bun):
    # add_ingredient добавляет один элемент в список ingredients
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
    # remove_ingredient удаляет по индексу, порядок оставшихся сохраняется.
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
    # move_ingredient переставляет элемент с old_index на позицию new_index.
    burger = Burger()
    burger.set_buns(mock_bun)
    for letter, price in [("a", 1), ("b", 2), ("c", 3)]:
        burger.add_ingredient(_make_ingredient_mock("SAUCE", letter, float(price)))
    burger.move_ingredient(old_index, new_index)
    assert [i.get_name() for i in burger.ingredients] == expected_order


def test_get_price_sums_bun_doubled_and_ingredients(mock_bun):
    # get_price: булка в двойном размере плюс сумма цен ингредиентов.
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(_make_ingredient_mock("SAUCE", "s1", 10))
    burger.add_ingredient(_make_ingredient_mock("FILLING", "f1", 5.5))
    assert burger.get_price() == 115.5
    mock_bun.get_price.assert_called()


def test_get_receipt_format_and_uses_getters(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    ing = _make_ingredient_mock("SAUCE", "Mayo", 20)
    burger.add_ingredient(ing)
    with patch.object(burger, "get_price", return_value=999.0):
        receipt = burger.get_receipt()
    assert receipt.startswith("(==== Sesame ====)")
    assert "= sauce Mayo =" in receipt
    assert "Price: 999.0" in receipt
    mock_bun.get_name.assert_called()
    ing.get_type.assert_called()
    ing.get_name.assert_called()

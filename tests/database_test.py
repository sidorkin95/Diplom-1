# Юнит-тесты класса Database
# Проверено: available_buns / available_ingredients отдают те же списки, что в классе
# каталог булок и ингредиентов по индексам; конструктор вызывает Bun и Ingredient (patch)

from unittest.mock import patch

import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def database():
    return Database()


def test_available_buns_returns_same_list_instance(database):
    buns = database.available_buns()
    assert buns is database.buns
    assert len(buns) == 3


def test_available_ingredients_returns_same_list_instance(database):
    ingredients = database.available_ingredients()
    assert ingredients is database.ingredients
    assert len(ingredients) == 6


@pytest.mark.parametrize(
    "index,name,price",
    [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ],
)
def test_database_bun_catalog(database, index, name, price):
    bun = database.available_buns()[index]
    assert bun.get_name() == name
    assert bun.get_price() == price


@pytest.mark.parametrize(
    "index,ingredient_type,name,price",
    [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ],
)
def test_database_ingredient_catalog(database, index, ingredient_type, name, price):
    ing = database.available_ingredients()[index]
    assert ing.get_type() == ingredient_type
    assert ing.get_name() == name
    assert ing.get_price() == price


@patch("praktikum.database.Bun")
@patch("praktikum.database.Ingredient")
def test_database_constructor_populates_via_models(mock_ingredient, mock_bun):
    Database()
    assert mock_bun.call_count == 3
    assert mock_ingredient.call_count == 6
    mock_bun.assert_any_call("black bun", 100)
    mock_ingredient.assert_any_call(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    mock_ingredient.assert_any_call(INGREDIENT_TYPE_FILLING, "sausage", 300)

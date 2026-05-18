import pytest

from praktikum.ingredient import Ingredient
from tests.constants import INGREDIENT_CASES


@pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_CASES)
def test_ingredient_get_type(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)

    assert ing.get_type() == ingredient_type


@pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_CASES)
def test_ingredient_get_name(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)

    assert ing.get_name() == name


@pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_CASES)
def test_ingredient_get_price(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)

    assert ing.get_price() == price

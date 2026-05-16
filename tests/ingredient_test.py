# Юнит-тесты класса Ingredient
# Проверено: get_type, get_name, get_price для разных типов

import pytest

from praktikum.ingredient import Ingredient


@pytest.mark.parametrize(
    "ingredient_type,name,price",
    [
        ("SAUCE", "hot sauce", 100.0),
        ("FILLING", "cutlet", 50.0),
        ("CUSTOM", "x", 0.0),
    ],
)
def test_ingredient_getters(ingredient_type, name, price):
    # Геттеры возвращают тип, имя и цену, переданные в конструктор
    ing = Ingredient(ingredient_type, name, price)
    assert ing.get_type() == ingredient_type
    assert ing.get_name() == name
    assert ing.get_price() == price


def test_ingredient_attributes_match_constructor():
    # Атрибуты экземпляра совпадают с параметрами конструктора
    ing = Ingredient("SAUCE", "chili", 300)
    assert ing.type == "SAUCE"
    assert ing.name == "chili"
    assert ing.price == 300

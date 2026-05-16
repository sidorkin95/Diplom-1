# Юнит-тесты класса Bun
# Проверено: get_name/get_price возвращают значения конструктора
# атрибуты name и price совпадают с переданными при создании булки

import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name,price",
    [
        ("black bun", 100.0),
        ("white bun", 200.5),
        ("", 0.0),
    ],
)
def test_bun_get_name_and_get_price(name, price):
    # Геттеры отдают имя и цену при создании
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_attributes_match_constructor():
    # Поля name и price совпадают с аргументами конструктора
    bun = Bun("red bun", 300)
    assert bun.name == "red bun"
    assert bun.price == 300

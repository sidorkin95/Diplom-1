import pytest

from praktikum.bun import Bun
from tests.constants import BUN_CASES


@pytest.mark.parametrize("name,price", BUN_CASES)
def test_bun_get_name(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name


@pytest.mark.parametrize("name,price", BUN_CASES)
def test_bun_get_price(name, price):
    bun = Bun(name, price)

    assert bun.get_price() == price


def test_bun_name_matches_constructor():
    bun = Bun("red bun", 300)

    assert bun.name == "red bun"


def test_bun_price_matches_constructor():
    bun = Bun("red bun", 300)

    assert bun.price == 300

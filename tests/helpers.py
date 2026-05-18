from unittest.mock import Mock


def _make_ingredient_mock(ing_type: str, name: str, price: float):
    m = Mock()
    m.get_type.return_value = ing_type
    m.get_name.return_value = name
    m.get_price.return_value = price
    return m

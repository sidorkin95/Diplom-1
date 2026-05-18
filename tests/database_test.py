def test_available_buns_returns_buns_list(database):
    assert database.available_buns() is database.buns


def test_available_ingredients_returns_ingredients_list(database):
    assert database.available_ingredients() is database.ingredients

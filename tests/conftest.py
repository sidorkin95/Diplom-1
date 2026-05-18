import pytest
from unittest.mock import Mock

from praktikum.database import Database


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Sesame"
    bun.get_price.return_value = 50.0
    return bun

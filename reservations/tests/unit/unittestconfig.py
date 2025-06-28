from unittest.mock import patch
import pytest


@pytest.fixture(autouse=True)
def disable_db_connection():
    """Desativa todas as tentativas de conexão com o banco"""
    with patch('sqlalchemy.create_engine'), \
         patch('sqlalchemy.orm.sessionmaker'):
        yield
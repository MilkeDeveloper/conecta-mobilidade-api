import pytest
from reservations.database import Base, engine

@pytest.fixture(autouse=True, scope="module")
def setup_db():
    """fixture para testes de integração"""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
import pytest
from reservations.models import BikeReservation
from reservations.tests.unit.unittestconfig import disable_db_connection

def test_reservation_default_status():
    """ test unitário utilizando banco de dados fake para verificar se a função retorna o comportamento esperado"""
    reservation = BikeReservation(
        user_id="user_645",
        bike_id="bike_956"
    )
    assert reservation.status == "pending" # testa apenas o default


def test_validate_status_valid():
    reservation = BikeReservation()
    result = reservation.validate_status("status", "confirmed")
    assert result == "confirmed"


def test_validate_status_invalid():
    reservation = BikeReservation()
    with pytest.raises(ValueError):
        reservation.validate_status("status", "invalid_value")

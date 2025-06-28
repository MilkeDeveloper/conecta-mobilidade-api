import pytest
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
from reservations.database import SessionLocal
from reservations.models import BikeReservation
from reservations.tests.integration.testconfig import setup_db


setup_db()

# teste para criar reserva no banco de dados
def test_create_reservation():
    with SessionLocal() as session:
        reservation = BikeReservation(
            user_id="milke123",
            bike_id="bike_002",
            station_id="station_001",
        )
        session.add(reservation)
        session.commit()

        assert reservation.id is not None
        assert reservation.status == "pending", (
            f"Status deveria ser Pending mas retornou {reservation.status}"
            f"Verifique o server_default no models e na tabela do banco de dados"
        ) # valor padrão
        from_db = session.get(BikeReservation, reservation.id)
        assert from_db.status == "pending"
        assert reservation.reserved_at <= datetime.now(timezone.utc)

# teste para verificar se a constraint CHECK do status está funcionando
def test_constraint_status():
    with SessionLocal() as session:
        invalid_reservation = BikeReservation(
            user_id="milke_xzw",
            bike_id="bike_adf",
            station_id="station_beta",
            status="invalid_status" # check inválido proposital
        )
        session.add(invalid_reservation)
        with pytest.raises(IntegrityError):
            session.commit()
        session.rollback()

# testa os campos NOT NULL
def test_required_fields():
    with SessionLocal() as session:
        invalid_fields = BikeReservation()
        session.add(invalid_fields)

        with pytest.raises(IntegrityError):
            session.commit()
        session.rollback()

# testa se o timestamp é preenchido automaticamente
def test_timestamp_auto_populate():
    with SessionLocal() as session:
        reservation = BikeReservation(
            user_id="user_fff",
            bike_id="bike_5874",
            station_id="station_gamma"
        )
        session.add(reservation)
        session.commit()

        assert reservation.reserved_at is not None
        assert reservation.reserved_at.tzinfo == timezone.utc # timezone UTC


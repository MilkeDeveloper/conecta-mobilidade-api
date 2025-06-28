from fastapi.params import Depends
from sqlalchemy.orm import Session

from reservations.database import get_db
from reservations.models import BikeReservation


class ReservationService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, user_id: str, bike_id: str, station_id: str):
        """Cria uma reserva com validações"""
        if not bike_id.startswith("bike_"):
            raise ValueError("ID de bike inválido")

        reservation = BikeReservation(
            user_id=user_id,
            bike_id=bike_id,
            station_id=station_id
        )
        self.db.add(reservation)
        self.db.commit()
        return reservation
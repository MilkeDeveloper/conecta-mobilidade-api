from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import BikeReservation

# teste para criar reserva no banco de dados

def test_create_reservation():
    db = SessionLocal()
    new_reservation = BikeReservation(
        user_id="milke123",
        bike_id="bike_002",
        station_id="station_001",
        status="pending"
    )
    db.add(new_reservation)
    db.commit()
    print(f"Peido de resrerva gerado: {new_reservation.id}")
    db.close()

if __name__ == "__main__":
    test_create_reservation()

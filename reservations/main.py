from fastapi import  FastAPI, Depends
from reservations.services.reservation_service import ReservationService

app = FastAPI()

@app.post("/reservations", status_code=201)
def create_reservation(
    user_id: str,
    bike_id: str,
    station_id: str,
    service: ReservationService = Depends(ReservationService)
):
    return service.create(user_id, bike_id, station_id)
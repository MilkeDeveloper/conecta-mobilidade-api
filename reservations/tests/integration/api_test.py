from fastapi.testclient import TestClient
from reservations.main import app

client = TestClient(app)

def test_create_reservation():
    response = client.post(
        "/reservations",
        params={
            "user_id": "user_axs",
            "bike_id": "bike_hju",
            "station_id": "station_alpha"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()
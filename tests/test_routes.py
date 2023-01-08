import pytest
from app.model.planet import Planet
from app.routes import validate_model

def test_get_planets_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_planet_with_id_returns_404(client):
    # Act
    response = client.get("/planets/100")

    # Assert 
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 100 not found"}


import pytest
from app.model.planet import Planet
from app.routes import validate_model

def test_get_planets_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

from werkzeug.exceptions import HTTPException
from app.models.planet import Planet
from app.routes import validate_model
import pytest

def test_read_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_read_one_planet_with_one_record(client, one_saved_planet):
    # Act
    response = client.get(f"/planets/{one_saved_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["description"] == one_saved_planet.description
    assert response_body["orbit_days"] == one_saved_planet.orbit_days
    assert response_body["num_moons"] == one_saved_planet.num_moons

def test_read_one_planet_with_no_records(client):
    # Act
    response = client.get(f"/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body["message"] == "Planet 1 not found"

def test_read_all_planets_with_one_record(client, one_saved_planet):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["id"] == one_saved_planet.id
    assert response_body[0]["name"] == one_saved_planet.name
    assert response_body[0]["description"] == one_saved_planet.description
    assert response_body[0]["orbit_days"] == one_saved_planet.orbit_days
    assert response_body[0]["num_moons"] == one_saved_planet.num_moons

def test_create_one_planet(client):
    # Act
    json_request_body = {
        "name": "Mars",
        "description": "Also known as Red planet.",
        "orbit_days": 687,
        "num_moons": 2
    }
    response = client.post("/planets", json=json_request_body)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"

def test_update_planet(client, one_saved_planet):
    # Arrange
    json_request_body = {
        "name": "Mars",
        "description": "Known as Red planet.",
        "orbit_days": 687,
        "num_moons": 2
    }

    # Act
    response = client.put("/planets/1", json=json_request_body)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"

def test_update_planet_missing_record(client, one_saved_planet):
    # Arrange
    json_request_body = {
        "name": "Earth",
        "description": "The best planet.",
        "orbit_days": 365,
        "num_moons": 1
    }

    # Act
    response = client.put("/planets/2", json=json_request_body)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 2 not found"}

def test_update_planet_invalid_id(client, one_saved_planet):
    # Arrange
    json_request_body = {
        "name": "Mars",
        "description": "Known as Red planet.",
        "orbit_days": 687,
        "num_moons": 2
    }

    # Act
    response = client.put("/planets/mars", json=json_request_body)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet mars invalid"}

def test_delete_planet(client, one_saved_planet):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"

def test_delete_planet_missing_record(client, one_saved_planet):
    # Act
    response = client.delete("/planets/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 2 not found"}

def test_delete_book_invalid_id(client, one_saved_planet):
    # Act
    response = client.delete("/planets/mars")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet mars invalid"}

def test_validate_model(one_saved_planet):
    # Act
    result_planet = validate_model(Planet, 1)

    # Assert
    assert result_planet.id == one_saved_planet.id
    assert result_planet.description == one_saved_planet.description
    assert result_planet.orbit_days == one_saved_planet.orbit_days
    assert result_planet.num_moons == one_saved_planet.num_moons

def test_validate_model_missing_record(one_saved_planet):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "2")
    
def test_validate_model_invalid_id(one_saved_planet):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "mars")
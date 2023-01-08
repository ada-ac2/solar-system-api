from werkzeug.exceptions import HTTPException
from app.models.moon import Moon
from app.models.planet import Planet
import pytest

#### POST/ Create moon for planet ####
def test_create_moon_for_planet_id_valid_request_return_201(client, one_planet): 
    # Arange
    planet_id = one_planet.id
    # Act
    response = client.post(f"/planets/{planet_id}/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "name": "Test1",
        "size": 3.6
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == f"Moon Test1 added to the planet {one_planet.name}."

def test_create_moon_for_planet_invalid_request_empty_name_return_400(client, one_planet):
    # Arange
    planet_id = one_planet.id
    # Act
    response = client.post(f"/planets/{planet_id}/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "size": 3.6,
        "planet_id": planet_id
        })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_moon_for_planet_invalid_request_size_zero_return_400(client, one_planet):
    # Arange
    planet_id = one_planet.id
    # Act
    response = client.post(f"/planets/{planet_id}/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "name": "Test1",
        "size": 0
        })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_moon_for_planet_invalid_request_description_empty_return_400(client, one_planet):
    # Arange
    planet_id = one_planet.id
    # Act
    response = client.post(f"/planets/{planet_id}/moons", json = {
        "name": "Test1",
        "size": 3.6
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

####GET moon inside of planet route####   
def test_get_moon_for_planet_by_id_for_planet_id_return_200(client,three_planets_with_moons):
    # Arange
    planet_id = 1
    moon_id = 1
    # Act
    response = client.get(f"planets/{planet_id}/moons/{moon_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Moon_Test1",
        "size": 173.1,
        "description": "Moon1 for testing purpose."
    }

def test_get_all_moons_for_planet_valid_planet_id_return_200_info_moons(client,three_planets_with_moons):
    # Arange
    planet_id = 1
    # Act
    response = client.get(f"planets/{planet_id}/moons")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == [
    {
        "id":1,
        "name": "Moon_Test1",
        "size": 173.1,
        "description": "Moon1 for testing purpose."
    },
    {
        "id":2,
        "name": "Moon_Test2",
        "size": 17.0,
        "description": "Moon2 just for testing."
    }
    ]

def test_get_all_moons_for_planet_by_not_exist_id_return_404(client, three_planets_with_moons):
    # Arange
    planet_id = 4
    # Act
    response = client.get(f"planets/{planet_id}/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == f"Planet {planet_id} not found"

def test_get_all_moons_for_planet_by_invalid_type_id_return_400(client, three_planets_with_moons):
    # Arange
    planet_id = "hello"
    # Act
    response = client.get(f"planets/{planet_id}/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == f"Planet {planet_id} invalid"

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

#### DELETE/ Delete moon for planet ####
def test_delete_moon_for_planet_by_id_valid_request_return_success_message(client, one_planet_with_moons):
    # Arange
    planet_id = 1
    moon_id = 1
    # Act
    response = client.delete(f"/{planet_id}/moons/{moon_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == f"Moon {moon_id} successfully deleted"

def test_delete_moon_by_id_invalid_id_return_400(client, one_moon):
    # Act
    moon_id = "hello"
    response = client.delete(f"/moons/{moon_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == f"Moon {moon_id} invalid"

def test_delete_moon_by_not_existed_id_return_404(client, one_moon):
    moon_id = 2
    response = client.delete(f"/moons/{moon_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert response_body == f"Moon {moon_id} not found"

####GET####   
def test_get_moon_by_id_return_200(client,one_moon):
    # Act
    response = client.get("/moons/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Test1",
        "size": 3.5,
        "description": "Fantasy moon for testing purpose."
    }

def test_get_all_moons_return_200(client,three_moons):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
    {
        "id":1,
        "name": "Test1",
        "size": 3.5,
        "description": "Fantasy moon for testing purpose."
    },
    {
        "id":2,
        "name": "Test2",
        "size": 4.0,
        "description": "Fantasy moon for testing purpose."
    },
    {
        "id":3,
        "name": "Test3",
        "size": 5.5,
        "description": "Fantasy moon for testing purpose."
    }
    ]

def test_get_moon_by_not_exist_did_return_404(client, one_moon):
    # Act
    response = client.get("/moons/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == "Moon 2 not found"

def test_get_moon_by_invalid_type_id_return_400(client,one_moon):
    # Act
    moon_id = "hello"
    response = client.get(f"/planets/{moon_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == f"Planet {moon_id} invalid"

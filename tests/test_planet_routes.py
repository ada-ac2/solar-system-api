from werkzeug.exceptions import HTTPException
from app.models.planet import Planet
import pytest

#### POST/ Create planet ####
def test_create_planet_valid_request_return_201(client):
    # Act
    response = client.post("/planets", json = {
        "description": "Mars is a dusty, cold, desert world with a very thin atmosphere.",
        "length_of_year": 687,
        "name": "Mars"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"

def test_create_planet_invalid_request_empty_name_return_400(client):
    # Act
    response = client.post("/planets", json = {
        "name": "", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_lenght_of_year_zero_return_400(client):
    # Act
    response = client.post("/planets", json = {
        "name": "Test", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 0})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_lenght_of_year_negative_return_400(client):
    # Act
    response = client.post("/planets", json = {
        'name': 'Test', 
        'description': 'This unknown planet is the imaginary planet for purpose of testing.', 
        'length_of_year': -100})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_description_empty_return_400(client):
    # Act
    response = client.post("/planets", json = {
        'name': 'Test', 
        'description': '', 
        'length_of_year': 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

#### PUT/ Update planet ####
def test_update_planet_valid_request_return_success_message(client, one_planet):
    # Act
    planet_id = one_planet.id
    response = client.put(f"/planets/{one_planet.id}", json = {
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "length_of_year": 88,
        "name": "Mercury_updated"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == f"Planet {planet_id} successfully updated"

def test_update_planet_not_exist_id_return_404(client, one_planet):
    # Act
    response = client.put("/planets/9", json = {
        "description": "Mars is a dusty, cold, desert world with a very thin atmosphere.",
        "length_of_year": 687,
        "name": "Mars"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == f"Planet 9 not found"

def test_update_planet_invalid_type_id_return_400(client, one_planet):
    # Act
    planet_id = "hello"
    response = client.put(f"/planets/{planet_id}", json = {
        "description": "Mars is a dusty, cold, desert world with a very thin atmosphere.",
        "length_of_year": 687,
        "name": "Mars"
    })
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == f"Planet {planet_id} invalid"

def test_update_planet_invalid_request_empty_name_return_400(client, one_planet):
    # Act
    response = client.put(f"/planets/{one_planet.id}", json = {
        "name": "", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_update_planet_invalid_request_lenght_of_year_zero_return_400(client, one_planet):
    # Act
    response = client.put(f"/planets/{one_planet.id}", json = {
        "name": "Test", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 0})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_update_planet_invalid_request_lenght_of_year_negative_return_400(client, one_planet):
    # Act
    response = client.put(f"/planets/{one_planet.id}", json = {
        'name': 'Test', 
        'description': 'This unknown planet is the imaginary planet for purpose of testing.', 
        'length_of_year': -100})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_update_planet_invalid_request_description_empty_return_400(client, one_planet):
    # Act
    response = client.put(f"/planets/{one_planet.id}", json = {
        'name': 'Test', 
        'description': '', 
        'length_of_year': 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

#### DELETE/ Delete planet ####
def test_delete_planet_by_id_valid_request_with_zero_moons_return_success_message(client, one_planet):
    # Act
    planet_id = one_planet.id
    response = client.delete(f"/planets/{planet_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == f"Planet {planet_id} successfully deleted"

def test_delete_planet_by_id_valid_request_with_two_moons_return_success_message(client, one_planet_with_moons):
    # Act
    planet_id = one_planet_with_moons.id
    response = client.delete(f"/planets/{planet_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == f"Planet {planet_id} successfully deleted"
    # Would like to add assert to check that moons deleted too 
    # dont know how 
    # will be happy to recieve the feedback :)

def test_delete_planet_by_invalid_type_id_return_400(client, one_planet):
    # Act
    planet_id = "hello"
    response = client.delete(f"/planets/{planet_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == f"Planet {planet_id} invalid"

def test_delete_planet_by_not_existed_id_return_404(client, one_planet):
    planet_id = 9
    response = client.delete(f"/planets/{planet_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert response_body == f"Planet {planet_id} not found"
    
#### GET/ Read one planet ####   
def test_get_planet_not_exist_id_return_404(client,one_planet):
    # Act
    response = client.get("/planets/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == f"Planet 2 not found"

def test_get_planet_invalid_type_id_return_400(client,one_planet):
    # Act
    planet_id = "hello"
    response = client.get(f"/planets/{planet_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == f"Planet {planet_id} invalid"

def test_get_planet_without_moons_valid_id_return_planet_info(client,three_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": []
    }

def test_get_planet_with_moon_valid_id_return_planet_info(client,one_planet_with_moons):
    # Act
    planet_id = one_planet_with_moons.id
    response = client.get(f"/planets/{planet_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": ["Moon_Test1", "Moon_Test2"]
    }

#### GET/ Read all planets ####   
def test_get_all_planets_without_moons_return_planets_info(client,three_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
    {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": []
    },
    {
        "id":2,
        "name": "Venus",
        "length_of_year": 225,
        "description": "Venus spins slowly in the opposite direction from most planets.",
        "moons": []
    },
    {
        "id":3,
        "name": "Earth",
        "length_of_year": 365,
        "description": "Earth — our home planet.",
        "moons": []
    }
]

def test_get_all_planets_with_moons_return_planets_info(client,three_planets_with_moons):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": ["Moon_Test1", "Moon_Test2"]
    },
    {
        "id":2,
        "name": "Venus",
        "length_of_year": 225,
        "description": "Venus spins slowly in the opposite direction from most planets.",
        "moons": ["Moon_Test3"]
    },
    {
        "id":3,
        "name": "Earth",
        "length_of_year": 365,
        "description": "Earth — our home planet.",
        "moons": ["Moon_Test4"]
    }
]

def test_get_all_planets_with_moons_sorted_by_name_return_planets_info(client,three_planets_with_moons):
    # Act
    data = {"sort": "name"}
    # Act
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [    
    {
        "id":3,
        "name": "Earth",
        "length_of_year": 365,
        "description": "Earth — our home planet.",
        "moons": ["Moon_Test4"]
    },
    {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": ["Moon_Test1", "Moon_Test2"]
    },
    {
        "id":2,
        "name": "Venus",
        "length_of_year": 225,
        "description": "Venus spins slowly in the opposite direction from most planets.",
        "moons": ["Moon_Test3"]
    }
]

def test_get_all_planets_with_moons_sorted_by_length_of_year_return_planets_info(client,three_planets_with_moons):
    # Act
    data = {"sort": "length_of_year"}
    # Act
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [    
    {
        "id":1,
        "name": "Mercury",
        "length_of_year": 88,
        "description": "Mercury is the smallest planet in the Solar System and the closest to the Sun.",
        "moons": ["Moon_Test1", "Moon_Test2"]
    },
    {
        "id":2,
        "name": "Venus",
        "length_of_year": 225,
        "description": "Venus spins slowly in the opposite direction from most planets.",
        "moons": ["Moon_Test3"]
    },
    {
        "id":3,
        "name": "Earth",
        "length_of_year": 365,
        "description": "Earth — our home planet.",
        "moons": ["Moon_Test4"]
    },
]
from werkzeug.exceptions import HTTPException
from app.models.moon import Moon
import pytest

#### POST/ Create moon ####
def test_create_moon_valid_request_return_201(client): 
    # Act
    response = client.post("/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "name": "Test1",
        "size": 3.6
    })
    response_body = response.get_json()
    # Assert
    assert response.status_code == 201
    assert response_body == "Moon Test1 successfully created"

def test_create_moon_invalid_request_empty_name_return_400(client):
    # Act
    response = client.post("/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "size": 3.6
        })
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_moon_invalid_request_size_zero_return_400(client):
    # Act
    response = client.post("/moons", json = {
        "description": "Fantasy moon for testing purpose.",
        "name": "Test1",
        "size": 0
        })
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_moon_invalid_request_description_empty_return_400(client):
    # Act
    response = client.post("/moons", json = {
        "name": "Test1",
        "size": 3.6
    })
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

#### DELETE/ Delete moon ####
def test_delete_moon_by_id_valid_request_return_success_message(client, one_moon):
    # Act
    moon_id = one_moon.id
    response = client.delete(f"/moons/{moon_id}")
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

####GET/ Read moon by id####   
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
    response = client.get(f"/moons/{moon_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == f"Moon {moon_id} invalid"

####GET/ Read all moons ####  
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

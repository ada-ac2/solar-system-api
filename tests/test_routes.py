from werkzeug.exceptions import HTTPException
from app.routes.planets_routes import validate_model
from app.models.planet import Planet
import pytest

#Tests on GET
def test_get_all_planets_with_empty_db_returns_empty_list(client):
    response = client.get("/planets")
    
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
            "id" : 1,
            "name": "Earth",
            "description": "rocky, terrestrial, full of life",
            "mass": 5.972e24
    }

def test_get_planet_by_id_with_empty_db_returns_404(client):
    response = client.get("/planets/1")
    
    assert response.status_code == 404
    assert response.get_json() == {"message" : "Planet 1 not found"}

def test_get_planet_by_invalid_id_returns_400(client, two_saved_planets):
    response = client.get("/planets/earth")
    
    assert response.status_code == 400
    assert response.get_json() == {"message":"Planet earth invalid"}

def test_get_planet_by_valid_data_returns_data_and_200(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {"name": "Earth",
        "description": "rocky, terrestrial, full of life",
        "mass": 5.972e24,
        "id": 1},
        {"name": "Mars",
        "description": "dusty, cold desert",
        "mass": 6.39e23,
        "id": 2}
    ]   

def test_get_mass_desc_and_limit_1_returns_data_and_200(client, two_saved_planets):
    response = client.get("/planets?sort=mass&desc=True&limit=1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "name": "Earth",
        "description": "rocky, terrestrial, full of life",
        "mass": 5.972e24,
        "id": 1
    }]

def test_get_name_desc_and_limit_1_returns_data_and_200(client, two_saved_planets):
    response = client.get("/planets?sort=name&desc=True&limit=1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "name": "Mars",
        "description": "dusty, cold desert",
        "mass": 6.39e23,
        "id": 2
    }]

def test_get_by_invalid_query_returns_error_message_and_400(client, two_saved_planets):
    response = client.get("/planets?hamster=True")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "hamster is an invalid query"}
 
#Tests on Post
def test_create_one_planet(client):
    response = client.post("/planets", json = {
        "name": "Neptune", 
        "description": "thick, windy", 
        "mass":1.024e26
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"message":"planet has been created successfully"}

def test_create_one_planet_missing_mass_return_400(client):
    response = client.post("/planets", json = {
        "name": "Neptune", 
        "description": "thick, windy"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message" : \
                "Failed to create a planet because mass missing"}

#Tests on Put
def test_update_planet_successfully(client, two_saved_planets):
    test_data = {"name" : "earth", 
            "description" : "terrestrial, full of life",     
            "mass" : 5.97e24}
    response = client.put("planets/1", json=test_data)
    
    assert response.status_code == 200
    assert response.get_json() == {"message": "Planet #1 successfully updated"}

def test_update_planet_with_extra_keys(client, two_saved_planets):
    test_data = {"name" : "earth", 
            "description" : "terrestrial, full of life",     
            "mass" : 5.97e24,
            "moon": "Moon"}

    response = client.put("planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"message": "Planet #1 successfully updated"}


def test_update_planet_missing_record(client, two_saved_planets):
    test_data = {
        "name": "Neptune", 
        "description": "thick, windy", 
        "mass":1.024e26
    }

    response = client.put("planets/3", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}


def test_update_planet_invalid_id(client, two_saved_planets):
    test_data = {
        "name": "Neptune", 
        "description": "thick, windy", 
        "mass":1.024e26
    }

    response = client.put("planets/cat", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

#Tests on Delete
def test_delete_planet_1_with_json_request_body_returns_200(client, two_saved_planets):
    response = client.delete("/planets/1", json={
        "name": "Earth",
        "description": "rocky, terrestrial, full of life",
        "mass": 5.972e24,
        "id": 1
    })
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {"message": "planet #1 has been deleted successfully"}

def test_delete_planet_missing_record(client, two_saved_planets):
    response = client.delete("planets/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_delete_planet_invalid_id(client, two_saved_planets):
    response = client.delete("planets/cat")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

#Tests on valid_model(cls, model_id)
def test_validate_model(two_saved_planets):
    result_planet = validate_model(Planet, 1)

    assert result_planet.id == 1
    assert result_planet.name == "Earth"
    assert result_planet.description == "rocky, terrestrial, full of life"
    assert result_planet.mass == 5.972e24

def test_validate_model_missing_record(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, 3)
    
def test_validate_model_invalid_id(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")
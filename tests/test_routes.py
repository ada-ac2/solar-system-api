from werkzeug.exceptions import HTTPException
from app.planet_routes import validate_model
from app.models.planet import Planet
import pytest

def test_get_planets_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_planet_with_id_empty_db_returns_404(client):
    # Act
    response = client.get("/planets/100")

    # Assert 
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 100 not found"}

def test_get_planets_optional_query_returns_seeded_planets(client, two_saved_planets):
    response = client.get("/planets")

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 1
    assert planet_list[0]["name"] == "Mars"
    assert planet_list[0]["description"] == "War planet"
    assert planet_list[0]["radius"] ==  2106.1
    assert planet_list[0]["num_moons"] == 2
    assert planet_list[0]["gravity"] == 3.721
    
    assert planet_list[1]["id"] == 2
    assert planet_list[1]["name"] == "Venus"
    assert planet_list[1]["description"] == "Planet Of Love"
    assert planet_list[1]["radius"] ==  3760.4
    assert planet_list[1]["num_moons"] == 1
    assert planet_list[1]["gravity"] == 8.874

def test_get_one_planet_with_name_param_asc_sort(client, two_saved_planets):
    response = client.get("/planets?name=Mars&sort=asc") 

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 1
    assert planet_list[0]["id"] == 1
    assert planet_list[0]["name"] == "Mars"
    assert planet_list[0]["description"] == "War planet"
    assert planet_list[0]["radius"] ==  2106.1
    assert planet_list[0]["num_moons"] == 2
    assert planet_list[0]["gravity"] == 3.721

def test_get_one_planet_with_name_param_desc_sort(client, two_saved_planets):
    response = client.get("/planets?name=Venus&sort=desc") 

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 1
    assert planet_list[0]["id"] == 2
    assert planet_list[0]["name"] == "Venus"
    assert planet_list[0]["description"] == "Planet Of Love"
    assert planet_list[0]["radius"] ==  3760.4
    assert planet_list[0]["num_moons"] == 1
    assert planet_list[0]["gravity"] == 8.874

def test_get_one_planet_by_id(client, two_saved_planets):
    response = client.get("/planets/2") 

    assert response.status_code == 200
    planet_list = response.get_json()
    assert planet_list["id"] == 2
    assert planet_list["name"] == "Venus"
    assert planet_list["description"] == "Planet Of Love"
    assert planet_list["radius"] ==  3760.4
    assert planet_list["num_moons"] == 1
    assert planet_list["gravity"] == 8.874

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "like the dog",
        "radius": 10000,
        "num_moons": 123,
        "gravity": 1234
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Pluto successfully created"

def test_delete_one_planet(client, two_saved_planets):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"


def test_does_not_delete_planet_with_invalid_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/helloworld")

    # Assert
    assert response.status_code == 400
    assert response.get_json() == {"message": f"Planet helloworld invalid"}

def test_does_not_delete_planet_with_nonexistent_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/100")

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 100 not found"}


def test_does_not_update_one_planet_with_invalid_id(client, two_saved_planets):
    # Act
    response = client.put("/planets/helloworld", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441,
        "num_moons":80,
        "gravity": 24.79
    })

    # Assert
    assert response.status_code == 400
    assert response.get_json() == {"message":f"Planet helloworld invalid"}

def test_does_not_update_one_planet_with_nonexistent_id(client, two_saved_planets):
    # Act
    response = client.put("/planets/300", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441,
        "num_moons":80,
        "gravity": 24.79
    })

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 300 not found"}

def test_update_one_planet(client, two_saved_planets):
    # Act
    response = client.put("/planets/2", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441,
        "num_moons":80,
        "gravity": 24.79
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #2 successfully updated"

def test_update_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441,
        "num_moons":80,
        "gravity": 24.79
    }

    # Act
    response = client.put("/planets/1", json=planet_data)
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"

def test_validate_model(two_saved_planets):
    # Act
    result_planet = validate_model(Planet, 2)

    # Assert
    assert result_planet.id == 2
    assert result_planet.name == "Venus"
    assert result_planet.description == "Planet Of Love"
    assert result_planet.radius ==  3760.4
    assert result_planet.num_moons == 1
    assert result_planet.gravity == 8.874

def test_validate_model_missing_id(two_saved_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")
    
def test_validate_model_invalid_id(two_saved_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "helloworld")
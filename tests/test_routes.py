import pytest
from app.model.planet import Planet
from app.routes import validate_model
#============================== test planets_bp.route =============================
#============================================================================

def test_get_planets_no_fixture_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_planet_with_id_no_fixture_returns_404(client):
    # Act
    response = client.get("/planets/100")

    # Assert 
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 100 not found"}

def test_get_planets_returns_seeded_planets(client, two_planets):
    response = client.get("/planets")

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 1
    assert planet_list[0]["name"] == "Earth"
    assert planet_list[0]["description"] == "Our planet"
    assert planet_list[0]["radius"] ==  3.95
    
    assert planet_list[1]["id"] == 2
    assert planet_list[1]["name"] == "Mars"
    assert planet_list[1]["description"] == "A dust,cold,desert world"
    assert planet_list[1]["radius"] ==  2.10
    
def test_get_planets_with_desc_sort(client, two_planets):
    response = client.get("/planets?sort=desc") 
    planet_list = response.get_json()

    assert response.status_code == 200
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 2
    assert planet_list[0]["name"] == "Mars"
    assert planet_list[0]["description"] == "A dust,cold,desert world"
    assert planet_list[0]["radius"] ==  2.10
    
    assert planet_list[1]["id"] == 1
    assert planet_list[1]["name"] == "Earth"
    assert planet_list[1]["description"] == "Our planet"
    assert planet_list[1]["radius"] ==  3.95

def test_get_planets_with_desc_sort(client, two_planets):
    response = client.get("/planets?sort=asc") 
    planet_list = response.get_json()

    assert response.status_code == 200
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 1
    assert planet_list[0]["name"] == "Earth"
    assert planet_list[0]["description"] == "Our planet"
    assert planet_list[0]["radius"] ==  3.95
    assert planet_list[1]["id"] == 2
    assert planet_list[1]["name"] == "Mars"
    assert planet_list[1]["description"] == "A dust,cold,desert world"
    assert planet_list[1]["radius"] ==  2.10

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Test1",
        "description": "1",
        "radius": 1
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Test1 successfully created"

def test_delete_one_planet(client, two_planets):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"


def test_does_not_delete_planet_with_invalid_id(client, two_planets):
    # Act
    response = client.delete("/planets/hhhh")

    # Assert
    assert response.status_code == 400
    assert response.get_json() == {"message": f"Planet hhhh invalid"}

def test_does_not_delete_planet_with_nonexistent_id(client, two_planets):
    # Act
    response = client.delete("/planets/100")

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 100 not found"}

def test_does_not_update_one_planet_with_invalid_id(client, two_planets):
    # Act
    response = client.put("/planets/helloworld", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441
    })

    # Assert
    assert response.status_code == 400
    assert response.get_json() == {"message":f"Planet helloworld invalid"}

def test_does_not_update_one_planet_with_nonexist_id(client, two_planets):
    # Act
    response = client.put("/planets/300", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441
    })

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 300 not found"}


def test_does_not_update_one_planet_with_return_200(client, two_planets):
    # Act
    response = client.put("/planets/1", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"

#============================== test moons_bp.route =============================
#============================================================================
def test_get_moons_no_fixture_returns_empty_list(client):
    # Act
    response = client.get("/moons")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []
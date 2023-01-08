import pytest
from app.model.planet import Planet
from app.routes import validate_model

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

def test_get_planets_returns_seeded_planets(client, two_saved_planets):
    response = client.get("/planets")

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 1
    assert planet_list[0]["name"] == "Mars"
    assert planet_list[0]["description"] == "War planet"
    assert planet_list[0]["radius"] ==  2106.1
    
    assert planet_list[1]["id"] == 2
    assert planet_list[1]["name"] == "Venus"
    assert planet_list[1]["description"] == "Planet Of Love"
    assert planet_list[1]["radius"] ==  3760.4
    
def test_get_planets_with_desc_sort(client, two_saved_planets):
    response = client.get("/planets?sort=desc") 

    assert response.status_code == 200
    planet_list = response.get_json()
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 2
    assert planet_list[0]["name"] == "Venus"
    assert planet_list[0]["description"] == "Planet Of Love"
    assert planet_list[0]["radius"] ==  3760.4
    
    assert planet_list[1]["id"] == 1
    assert planet_list[1]["name"] == "Mars"
    assert planet_list[1]["description"] == "War planet"
    assert planet_list[1]["radius"] ==  2106.1

def test_get_one_planet_by_id(client, two_saved_planets):
    response = client.get("/planets/2") 

    assert response.status_code == 200
    planet_list = response.get_json()
    assert planet_list["id"] == 2
    assert planet_list["name"] == "Venus"
    assert planet_list["description"] == "Planet Of Love"
    assert planet_list["radius"] ==  3760.4

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "like the dog",
        "radius": 10000
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
        "radius": 43441
    })

    # Assert
    assert response.status_code == 400
    assert response.get_json() == {"message":f"Planet helloworld invalid"}

def test_does_not_update_one_planet_with_nonexist_id(client, two_saved_planets):
    # Act
    response = client.put("/planets/300", json={
        "name": "Jupiter",
        "description": "Planet Of Luck",
        "radius": 43441
    })

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message":f"Planet 300 not found"}

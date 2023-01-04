import pytest
from app.models.planet import Planet

def test_get_planets_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_planets_optional_query_returns_seeded_planet(client, two_planets):
    response = client.get("/planets")
    planet_list = response.get_json()

    assert response.status_code == 200
    assert len(planet_list) == 2
    assert planet_list[0]["id"] == 1 
    assert planet_list[0]["name"] == "Earth"
    assert planet_list[0]["description"] == "habitable"
    assert planet_list[0]["diameter_in_km"] == 12756

    assert planet_list[1]["id"] == 2 
    assert planet_list[1]["name"] == "Mars"
    assert planet_list[1]["description"] == "inhabitable"
    assert planet_list[1]["diameter_in_km"] == 6792

def test_get_planet_optional_query_missing_record_returns_404(client, two_planets):
    response = client.get("/planets/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet #3 not found"}

def test_get_planet_by_id_returns_200_with_matching_response(client, two_planets):
    response = client.get("/planets/1")
    planet_list = response.get_json()

    assert response.status_code == 200
    assert planet_list == {
        "id": 1,
        "name": "Earth",
        "description": "habitable",
        "diameter_in_km": 12756
    }

def test_get_planet_by_id_invalid_id_returns_400(client, two_planets):
    # Act
    response = client.get("/planets/earth")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet #earth is not an int."}

def test_create_planet_returns_201(client):
    test_data = {
        "name": "Mercury", 
        "description": "inhabitable", 
        "diameter_in_km": 4879
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Mercury successfully created"

def test_update_planet_returns_200(client, two_planets):
    test_data = {
        "name": "Mercury", 
        "description": "inhabitable", 
        "diameter_in_km": 4879
    }

    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated."

def test_update_planet_invalid_id_returns_400(client, two_planets):
    test_data = {
        "name": "Mercury", 
        "description": "inhabitable", 
        "diameter_in_km": 4879
    }

    response = client.put("/planets/earth", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet #earth is not an int."}

def test_delete_planet_returns_200(client, two_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"

def test_delete_planet_returns_404(client, two_planets):
    response = client.delete("/planets/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet #3 not found"}

def test_delete_planet_invalid_id_returns_400(client, two_planets):
    response = client.delete("/planets/earth")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet #earth is not an int."}

def test_update_planet_missing_planet_returns_404(client, two_planets):
    test_data = {
        "name": "Mercury", 
        "description": "inhabitable", 
        "diameter_in_km": 4879
    }

    response = client.put("/planets/3", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet #3 not found"}

def test_create_planet_missing_name_attribute(client, two_planets):
    test_data = {
        "description": 'habitable', 
        "diameter_in_km": 12345
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()
    assert response.status_code == 400 
    assert response_body == {"message":"Missing name."}

def test_create_planet_missing_description_attribute(client, two_planets):
    test_data = {
        "name": "Mars", 
        "diameter_in_km": 12345
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()
    assert response.status_code == 400 
    assert response_body == {"message":"Missing description."}

def test_create_planet_missing_diameter_in_km_attribute(client):
    test_data = {
        "name": "Mars",
        "description": 'habitable'
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()
    assert response.status_code == 400 
    assert response_body == {"message":"Missing diameter_in_km."}
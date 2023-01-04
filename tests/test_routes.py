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
    assert response_body["message"] == "planet 1 not found"

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
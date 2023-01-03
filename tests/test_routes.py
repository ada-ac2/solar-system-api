def test_get_planets_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []
    

def test_create_one_planet(client):
    #Act
    response = client.post("/planets", json={
        "name": "Mercury",
        "description": "is the smallest planet in the Solar System",
        "color": "gray"
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == "Planet Mercury created."

def test_replace_one_planet(client, saved_two_planets):
    #Arrange
    test_data = {
        "name": "Mars",
        "description": "Still a planet in our hearts"
    }

    #Act
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated."

def test_replace_planet_id_not_found(client, saved_two_planets):
    #Arrange
    test_data = {
        "name": "Mars",
        "description": "Still a planet in our hearts"
    }

    #Act
    response = client.put("/planets/9", json=test_data)
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 404
    assert response_body == {"message": "planet_id 9 not found."}

def test_delete_one_planet(client, saved_two_planets):
    #Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted."

def test_delete_planet_id_not_found(client, saved_two_planets):
    #Act
    response = client.delete("/planets/5")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 404
    assert response_body == {"message": "planet_id 5 not found."}

def test_delete_planet_invalid(client, saved_two_planets):
    #Act
    response = client.delete("/planets/cat")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 400
    assert response_body == {"message": "planet_id cat is invalid."}
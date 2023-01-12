def test_get_all_planets_with_empty_db_returns_empty_list(client):
    response = client.get("/planets")
    
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
            "id" : 1,
            "name": "Earth",
            "description": "rocky, terrestrial, full of life",
            "mass": 5.972e24
    }

def test_create_one_planet(client):
    #Act
    response = client.post("/planets", json = {
         "name": "Neptune", 
         "description": "thick, windy", 
         "mass":1.024e26
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == {"message":"planet has been created successfully"}

def test_create_one_planet_missing_mass_return_400(client):
    #Act
    response = client.post("/planets", json = {
         "name": "Neptune", 
         "description": "thick, windy"
    })
    response_body = response.get_json()
    #Assert
    assert response.status_code == 400
    assert response_body == {"message" : \
                "Failed to create a planet because the name and/or description \
                and/or mass are missing"}


def test_get_planet_by_id_with_empty_db_returns_404(client):
    response = client.get("/planets/1")
    
    assert response.status_code == 404
    assert response.get_json() == {"message" : "1 not found"}


def test_update_planet_successfully(client, two_saved_planets):
    test_data = {"name" : "earth", 
            "description" : "terrestrial, full of life",     
            "mass" : 5.97e24}
    response = client.put("planets/1", json=test_data)
    
    assert response.status_code == 200
    assert response.get_json() == {"message": "planet #1 Updated Successfully"}


def test_get_planet_by_invalid_id_returns_400(client, two_saved_planets):
    response = client.get("/planets/earth")
    
    assert response.status_code == 400
    assert response.get_json() == {"message": "earth is an invalid planet id"}

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

def test_delete_planet_1_with_json_request_body_returns_200(client, two_saved_planets):
    response = client.delete("/planets/1", json={
        "name": "Earth",
        "description": "rocky, terrestrial, full of life",
        "mass": 5.972e24,
        "id": 1
    })
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {"message": f"planet #1 has been deleted successfully"}, 200

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

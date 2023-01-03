def test_get_planets_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []
    

# GET /planets/1 returns a 200 with a response 
# body that matches our fixture
def test_get_one_planet(client, saved_two_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert response_body == {
                                "id" : 1,
                                "name" : "Mercury",
                                "color" : "gray",
                                "description" : "is the smallest planet in the Solar System"
                            }

# GET /planets/1 with no data in test database 
# (no fixture) returns a 404
def test_get_one_no_data_planet(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == {'message': 'planet_id 1 not found.'} 


# GET /planets with valid test data (fixtures) 
# returns a 200 with an array including appropriate test data
def test_get_all_planets_with_valid_data(client, saved_two_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert response_body ==[
                        {
                            "id" : 1,
                            "name" : "Mercury",
                            "color" : "gray",
                            "description" : "is the smallest planet in the Solar System"
                        },
                                                {
                            "id" : 2,
                            "name" : "Earth",
                            "color" : "blue",
                            "description" : "The planet that we live on"
                        }
            ]
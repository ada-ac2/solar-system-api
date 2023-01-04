def test_create_planet_valid_request(client):
    # Act
    response = client.post("/planets", json = {
        "description": "Mars is a dusty, cold, desert world with a very thin atmosphere.",
        "length_of_year": 687,
        "name": "Mars"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"

def test_create_planet_invalid_request_empty_name(client):
    # Act
    response = client.post("/planets", json = {
        "name": "", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_lenght_of_year_zero(client):
    # Act
    response = client.post("/planets", json = {
        "name": "Test", 
        "description": "This unknown planet is the imaginary planet for purpose of testing.", 
        "length_of_year": 0})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_lenght_of_year_negative(client):
    # Act
    response = client.post("/planets", json = {
        'name': 'Test', 
        'description': 'This unknown planet is the imaginary planet for purpose of testing.', 
        'length_of_year': -100})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"

def test_create_planet_invalid_request_description_empty(client):
    # Act
    response = client.post("/planets", json = {
        'name': 'Test', 
        'description': '', 
        'length_of_year': 10})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == "Invalid request"
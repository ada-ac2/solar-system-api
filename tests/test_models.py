from app.models.planet import Planet
import pytest


def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        'name': "Earth", 
        'description':"habitable", 
        'diameter_in_km': 12756
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Earth"
    assert new_planet.description == "habitable"
    assert new_planet.diameter_in_km == 12756

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        'description':"habitable", 
        'diameter_in_km': 12756
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Earth",
        'diameter_in_km': 12756
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        'name': "Earth", 
        'description':"habitable", 
        'diameter_in_km': 12756,
        'has_air': True
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == 'Earth'
    assert new_planet.description == "habitable"
    assert new_planet.diameter_in_km == 12756

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
        id = 1,
        name = "Earth", 
        description = "habitable", 
        diameter_in_km = 12756)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "habitable"
    assert result["diameter_in_km"] == 12756

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
        name = "Earth", 
        description = "habitable", 
        diameter_in_km = 12756)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] is None
    assert result["name"] == "Earth"
    assert result["description"] == "habitable"
    assert result["diameter_in_km"] == 12756

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description = "habitable", 
                    diameter_in_km = 12756)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "habitable"
    assert result["diameter_in_km"] == 12756

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name = "Earth", 
                    diameter_in_km = 12756)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] is None
    assert result["diameter_in_km"] == 12756

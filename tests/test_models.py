# from werkzeug.exceptions import HTTPException
from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    #Arrange
    test_data = Planet(
                id = 1,
                name = "Mercury",
                color = "gray",
                description = "is the smallest planet in the Solar System"
                )

    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["color"] == "gray"
    assert result["description"] == "is the smallest planet in the Solar System"

def test_to_dict_missing_name():
    #Arrange
    test_data = Planet(
                id = 1,
                color = "gray",
                description = "is the smallest planet in the Solar System"
                )

    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["color"] == "gray"
    assert result["description"] == "is the smallest planet in the Solar System"

def test_to_dict_missing_color():
    #Arrange
    test_data = Planet(
                id = 1,
                name = "Mercury",
                description = "is the smallest planet in the Solar System"
                )

    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["color"] is None
    assert result["description"] == "is the smallest planet in the Solar System"

def test_to_dict_missing_description():
    #Arrange
    test_data = Planet(
                id = 1,
                name = "Mercury",
                color = "gray",
                )

    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["color"] == "gray"
    assert result["description"] is None

def test_to_dict_missing_id():
    #Arrange
    test_data = Planet(
                name = "Mercury",
                color = "gray",
                description = "is the smallest planet in the Solar System"
                )

    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["color"] == "gray"
    assert result["description"] == "is the smallest planet in the Solar System"


def test_from_dict_return_planet():
    #Arrange
    planet_data = {
            "name": "Mercury",
            "description": "is the smallest planet in the Solar System",
            "color":"gray"
        }

    #Act
    new_planet = Planet.from_dict(planet_data)

    #Assert
    assert new_planet.name == "Mercury"
    assert new_planet.color == "gray"
    assert new_planet.description == "is the smallest planet in the Solar System"

def test_from_dict_missing_name():
    #Arrange
    planet_data = {
            "description": "is the smallest planet in the Solar System",
            "color":"gray"
        }

    #Act, Assert
    with pytest.raises(KeyError, match = "name"):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_missing_color():
    #Arrange
    planet_data = {
            "name": "Mercury",
            "description": "is the smallest planet in the Solar System",
        }

    #Act, Assert
    with pytest.raises(KeyError, match="color"):
        new_planet = Planet.from_dict(planet_data)



def test_from_dict_missing_description():
    #Arrange
    planet_data = {
            "name": "Mercury",
            "color":"gray"
        }

    #Act, Assert
    with pytest.raises(KeyError, match="description"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_extra_key():
    #Arrange
    planet_data = {
            "name": "Mercury",
            "description": "is the smallest planet in the Solar System",
            "color":"gray",
            "aliens": "yes"
        }

    #Act
    new_planet = Planet.from_dict(planet_data)

    #Assert
    assert new_planet.name == "Mercury"
    assert new_planet.color == "gray"
    assert new_planet.description == "is the smallest planet in the Solar System"
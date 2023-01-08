from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.planet_routes import validate_model
from werkzeug.exceptions import HTTPException
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    moon1 = Moon(
        description = "Earth's Moon is the only place beyond Earth where humans have set foot, so far.",
        size = 1738.1,
        name = "Moon"
    )

    test_data = Planet(
                    name="Test",
                    moons = [moon1],
                    description="Imaginary for testing",
                    length_of_year = 100)
    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 5
    assert result["moons"] == ["Moon"]
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_id():
    # Arrange
    moon1 = Moon(
        description = "Earth's Moon is the only place beyond Earth where humans have set foot, so far.",
        size = 1738.1,
        name = "Moon"
    )
    test_data = Planet(name="Test",
                    description="Imaginary for testing",
                    length_of_year = 100,
                    moons = [moon1]
                    )
    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 5
    assert result["name"] == "Test"
    assert result["moons"] == ["Moon"]
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_name():
    # Arrange
    moon1 = Moon(
        description = "Earth's Moon is the only place beyond Earth where humans have set foot, so far.",
        size = 1738.1,
        name = "Moon"
    )

    test_data = Planet(
                    moons = [moon1],
                    description="Imaginary for testing",
                    length_of_year = 100)

    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 5
    assert result["moons"] == ["Moon"]
    assert result["name"] == None
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_description():
    # Arrange
    moon1 = Moon(
        description = "Earth's Moon is the only place beyond Earth where humans have set foot, so far.",
        size = 1738.1,
        name = "Moon"
    )

    test_data = Planet(
                    name="Test",
                    moons = [moon1],
                    length_of_year = 100)

    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 5
    assert result["moons"] == ["Moon"]
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == None

def test_to_dict_missing_moon():
    # Arrange
    moon1 = Moon(
        description = "Earth's Moon is the only place beyond Earth where humans have set foot, so far.",
        size = 1738.1,
        name = "Moon"
    )

    test_data = Planet(
                    name="Test",
                    description="Imaginary for testing",
                    length_of_year = 100)

    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 5
    assert result["moons"] == []
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_from_dict_returns_planet():
# Arrange
    planet_data = {
        "name": "Test",
        "length_of_year": 100,
        "description": "Imaginary for testing"
    }
# Act
    new_planet = Planet.from_dict(planet_data)
# Assert
    assert new_planet.name == "Test"
    assert new_planet.length_of_year == 100
    assert new_planet.description == "Imaginary for testing"

def test_from_dict_with_no_name():
# Arrange
    planet_data = {
        "length_of_year": 100,
        "description": "Imaginary for testing"
    }
# Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
# Arrange
    planet_data = {
        "name": "Test",
        "length_of_year": 100,
    }
# Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
# Arrange
    planet_data = {
        "name": "Test",
        "length_of_year": 100,
        "description": "Imaginary for testing"
    }
# Act
    new_planet = Planet.from_dict(planet_data)
# Assert
    assert new_planet.name == "Test"
    assert new_planet.length_of_year == 100
    assert new_planet.description == "Imaginary for testing"

#### tests for validate_model ####
def test_validate_model(three_planets):
    # Act
    result_planet = validate_model(Planet, 1)
    # Assert
    assert result_planet.id == 1
    assert result_planet.name == "Mercury"
    assert result_planet.length_of_year == 88
    assert result_planet.description == "Mercury is the smallest planet in the Solar System and the closest to the Sun."

def test_validate_model_missing_record(three_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, 9)
    
def test_validate_model_invalid_id(three_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "hello")

#### tests for validate_input ####
from app import db
from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
                    name="Test",
                    description="Imaginary for testing",
                    length_of_year = 100)

    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 4
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Test",
                    description="Imaginary for testing",
                    length_of_year = 100
                    )
    # Act
    result = test_data.to_dict()
    # Assert
    assert len(result) == 4
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_name():
# Arrange
    test_data = Planet(
                    description="Imaginary for testing",
                    length_of_year = 100
                    )

# Act
    result = test_data.to_dict()
# Assert
    assert len(result) == 4
    assert result["name"] == None
    assert result["length_of_year"] == 100
    assert result["description"] == "Imaginary for testing"

def test_to_dict_missing_description():
# Arrange
    test_data = Planet(name="Test",
                    length_of_year = 100)
# Act
    result = test_data.to_dict()
# Assert
    assert len(result) == 4
    assert result["name"] == "Test"
    assert result["length_of_year"] == 100
    assert result["description"] == None

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
        "description": "Imaginary for testing",
        "number_of_moons": 9
    }
# Act
    new_planet = Planet.from_dict(planet_data)
# Assert
    assert new_planet.name == "Test"
    assert new_planet.length_of_year == 100
    assert new_planet.description == "Imaginary for testing"
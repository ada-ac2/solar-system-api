from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    planet_data = Planet(
        id = 1,
        name =  "Mars",
        description = "Also known as Red planet.",
        orbit_days = 687,
        num_moons = 2
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "Also known as Red planet."
    assert result["orbit_days"] == 687
    assert result["num_moons"] == 2

def test_to_dict_missing_id():
    # Arrange
    planet_data = Planet(
        name =  "Mars",
        description = "Also known as Red planet.",
        orbit_days = 687,
        num_moons = 2
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == None
    assert result["name"] == "Mars"
    assert result["description"] == "Also known as Red planet."
    assert result["orbit_days"] == 687
    assert result["num_moons"] == 2

def test_to_dict_missing_name():
    # Arrange
    planet_data = Planet(
        id = 1,
        description = "Also known as Red planet.",
        orbit_days = 687,
        num_moons = 2
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Also known as Red planet."
    assert result["orbit_days"] == 687
    assert result["num_moons"] == 2

def test_to_dict_missing_description():
    # Arrange
    planet_data = Planet(
        id = 1,
        name = "Mars",
        orbit_days = 687,
        num_moons = 2
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["orbit_days"] == 687
    assert result["num_moons"] == 2

def test_to_dict_missing_orbit_days():
    # Arrange
    planet_data = Planet(
        id = 1,
        name = "Mars",
        description = "Also known as Red planet.",
        num_moons = 2
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "Also known as Red planet."
    assert result["orbit_days"] is None
    assert result["num_moons"] == 2

def test_to_dict_missing_num_moons():
    # Arrange
    planet_data = Planet(
        id = 1,
        name = "Mars",
        description = "Also known as Red planet.",
        orbit_days = 687,
    )

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "Also known as Red planet."
    assert result["orbit_days"] == 687
    assert result["num_moons"] is None

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name":  "Mars",
        "description": "Also known as Red planet.",
        "orbit_days": 687,
        "num_moons": 2
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "Also known as Red planet."
    assert new_planet.orbit_days == 687
    assert new_planet.num_moons == 2

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "Also known as Red planet.",
        "orbit_days": 687,
        "num_moons": 2
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mars",
        "orbit_days": 687,
        "num_moons": 2
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_orbit_days():
    # Arrange
    planet_data = {
        "name": "Mars",
        "description": "Also known as Red planet.",
        "num_moons": 2
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'orbit_days'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_num_moons():
    # Arrange
    planet_data = {
        "name": "Mars",
        "description": "Also known as Red planet.",
        "orbit_days": 687,
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'num_moons'):
        new_planet = Planet.from_dict(planet_data)
from app.planet_routes import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    description="watr 4evr",
                    radius=2106.1,
                    num_moons=2,
                    gravity=3.721
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "watr 4evr"
    assert result["radius"] == 2106.1
    assert result["num_moons"] == 2
    assert result["gravity"] == 3.721


def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mars",
                    description="watr 4evr",
                    radius=2106.1,
                    num_moons=2,
                    gravity=3.721
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "watr 4evr"
    assert result["radius"] == 2106.1
    assert result["num_moons"] == 2
    assert result["gravity"] == 3.721

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="watr 4evr",
                    radius=2106.1,
                    num_moons=2,
                    gravity=3.721
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "watr 4evr"
    assert result["radius"] == 2106.1
    assert result["num_moons"] == 2
    assert result["gravity"] == 3.721

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id=2,
                    name="Mars",
                    radius=2106.1,
                    num_moons=2,
                    gravity=3.721
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 2
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["radius"] == 2106.1
    assert result["num_moons"] == 2
    assert result["gravity"] == 3.721

def test_to_dict_missing_radius():
    # Arrange
    test_data = Planet(id=2,
                    name="Mars",
                    description="watr 4evr",
                    num_moons=2,
                    gravity=3.721
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 2
    assert result["name"] == "Mars"
    assert result["description"] == "watr 4evr"
    assert result["radius"] is None
    assert result["num_moons"] == 2
    assert result["gravity"] == 3.721

def test_to_dict_missing_number_of_moons():
    # Arrange
    test_data = Planet(id=2,
                    name="Mars",
                    description="watr 4evr",
                    radius=2106.1,
                    gravity=3.721
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 2
    assert result["name"] == "Mars"
    assert result["description"] == "watr 4evr"
    assert result["radius"] == 2106.1
    assert result["num_moons"] is None
    assert result["gravity"] == 3.721

def test_to_dict_missing_gravity():
    # Arrange
    test_data = Planet(id=2,
                    description="watr 4evr",
                    name="Mars",
                    radius=2106.1,
                    num_moons=2,
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 2
    assert result["name"] == "Mars"
    assert result["description"] == "watr 4evr"
    assert result["radius"] == 2106.1
    assert result["num_moons"] == 2
    assert result["gravity"] is None

# from_dict tests

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
                    "name": "Mars",
                    "description": "watr 4evr",
                    "radius": 2106.1,
                    "num_moons": 2,
                    "gravity": 3.721
                }
    
    # Act
    result = Planet.from_dict(planet_data)

    # Assert
    assert result.name == "Mars"
    assert result.description == "watr 4evr"
    assert result.radius == 2106.1
    assert result.num_moons == 2
    assert result.gravity == 3.721

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
                    "description": "watr 4evr",
                    "radius": 2106.1,
                    "num_moons": 2,
                    "gravity": 3.721
                }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        result = Planet.from_dict(planet_data)


def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mars",
        "radius": 2106.1,
        "num_moons": 2,
        "gravity": 3.721
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        result = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "name": "Mars",
        "description": "watr 4evr",
        "radius": 2106.1,
        "num_moons": 2,
        "gravity": 3.721,
        "extra": "new stuff"
    }
    
    # Act
    result = Planet.from_dict(planet_data)

    # Assert
    assert result.name == "Mars"
    assert result.description == "watr 4evr"
    assert result.radius == 2106.1
    assert result.num_moons == 2
    assert result.gravity == 3.721

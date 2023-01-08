from app.model.planet import Planet
from app.model.moon import Moon
import pytest
#==============================test Planet model=============================
#=========== =================================================================
def test_planet_model_to_dict_no_missing_data():
    
    moon1 = Moon(
        description = "Earth's Moon",
        size = "small",
        name = "Moon"
    )
    test_data = Planet(id = 1, 
                       name="Earth", 
                       description="Our planet", 
                       radius=3.95, 
                       moons=[moon1])
            
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "Our planet"
    assert result["radius"] == 3.95
    assert result["moons"] == ["Moon"]

def test_planet_model_to_dict_missing_name():
    # Arrange
   
    test_data = Planet(id = 1,
                    name="",
                    description="Our planet",
                    radius=3.95
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] =="" 
    assert result["description"] == "Our planet"
    assert result["radius"] == 3.95

def test_planet_model_to_dict_missing_description():
    # Arrange
   
    test_data = Planet(id = 1,
                    name="Earth",
                    description="",
                    radius=3.95
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["description"] == ""
    assert result["name"] == "Earth"
    assert result["radius"] == 3.95



def test_planet_model_to_dict_missing_radius():
    # Arrange
   
    test_data = Planet(id = 1,
                    name="Earth",
                    description="Our planet",
                    radius=""
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["description"] == "Our planet"
    assert result["name"] == "Earth"
    assert result["radius"] == ""

def test_planet_from_dict_returns_planet():
    # Arrange
    planet_data = {
                    "name": "Earth",
                    "description": "Our planet",
                    "radius": 3.95,}
    
    # Act
    result = Planet.from_dict(planet_data)

    # Assert
    assert result.name == "Earth"
    assert result.description == "Our planet"
    assert result.radius == 3.95

def test_planet_from_dict_no_name():
    # Arrange
    planet_data = {"description": "Our planet",
                    "radius": 3.95,}
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        result = Planet.from_dict(planet_data)

def test_planet_from_dict_no_description():
    # Arrange
    planet_data = {"name":"Earth",
                    "radius": 3.95,}
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        result = Planet.from_dict(planet_data)

def test_planet_from_dict_no_radius():
    # Arrange
    planet_data = {"name":"Earth",
                   "description": "Our planet"}
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'radius'):
        result = Planet.from_dict(planet_data)


#==============================test Moon model=============================
#============================================================================

def test_moon_model_to_dict_no_missing_data():
    # Arrange
   
    test_data = Moon(id = 1,
                    name="Moon 1",
                    description="Moon 1 is small",
                    size = "small"
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Moon 1"
    assert result["description"] == "Moon 1 is small"
    assert result["size"] == "small"

def test_moon_model_to_dict_missing_name():
    # Arrange
   
    test_data = Moon(id = 1,
                    name="",
                    description="Moon 1 is small",
                    size = "small"
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == ""
    assert result["description"] == "Moon 1 is small"
    assert result["size"] == "small"

def test_moon_model_to_dict_missing_size():
    # Arrange
   
    test_data = Moon(id = 1,
                    name="",
                    description="Moon 1 is small",
                    size = ""
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == ""
    assert result["description"] == "Moon 1 is small"
    assert result["size"] == ""


def test_moon_model_to_dict_missing_description():
    # Arrange
   
    test_data = Moon(id = 1,
                    name="Moon1",
                    description="",
                    size = "small"
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Moon1"
    assert result["description"] == ""
    assert result["size"] == "small"

def test_moon_from_dict_returns_moon():
    # Arrange
    moon_data = {
                    "name": "Moon1",
                    "description": "Moon 1 is small",
                    "size": "small",}
    
    # Act
    result = Moon.from_dict(moon_data)

    # Assert
    assert result.name == "Moon1"
    assert result.description == "Moon 1 is small"
    assert result.size == "small"

def test_moon_from_dict_no_name():
    # Arrange
    test_data = {"description":"Moon 1 is small",
                "size" :"small"
    }
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        result = Moon.from_dict(test_data)

def test_moon_from_dict_no_size():
    # Arrange
    test_data = {"name":"Moon1",
                "description":"Moon 1 is small"}
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'size'):
        result = Moon.from_dict(test_data)

def test_moon_from_dict_no_description():
    # Arrange
    test_data = {"name":"Moon1",
                "size":"small"}
    
    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        result = Moon.from_dict(test_data)
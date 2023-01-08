from app.model.planet import Planet
from app.model.moon import Moon
import pytest
#==============================test Planet model=============================
#============================================================================
def test_planet_model_to_dict_no_missing_data():
    # Arrange
   
    test_data = Planet(id = 1,
                    name="Earth",
                    description="Our planet",
                    radius=3.95
                    )
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "Our planet"
    assert result["radius"] == 3.95

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
    assert len(result) == 4
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
    assert len(result) == 4
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
    assert len(result) == 4
    assert result["id"] == 1
    assert result["description"] == "Our planet"
    assert result["name"] == "Earth"
    assert result["radius"] == ""

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

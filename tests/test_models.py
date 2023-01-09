from app.models.planet import Planet
import pytest


def test_from_dict_with_valid_input():
    test_data = {
        "name" : "Neptune",
        "description" : "thick, windy",
        "mass" : 1.024e26
    }
    result = Planet.from_dict(test_data)

    assert result.name == "Neptune"
    assert result.description == "thick, windy"
    assert result.mass == 1.024e26


def test_from_dict_without_given_name():
    test_data = {"description" : "thick, windy",
            "mass" : 1.024e26}

    with pytest.raises(KeyError, match="name"):
        Planet.from_dict(test_data)


def test_from_dict_without_given_mass():
    test_data = {"description" : "thick, windy",
            "name":"Neptune"}

    with pytest.raises(KeyError, match="mass"):
        Planet.from_dict(test_data)

def test_from_dict_without_given_description():
    test_data = {
        "name" : "Neptune",
        "mass" : 1.024e26
    }

    with pytest.raises(KeyError, match="description"):
        Planet.from_dict(test_data)


def test_from_dict_with_extra_input():
    test_data = {
        "name" : "Neptune",
        "description" : "thick, windy",
        "mass" : 1.024e26,
        "extra1" : "extra info",
        "extra2" : "more extra info"
    }

    result = Planet.from_dict(test_data)

    assert result.name == "Neptune"
    assert result.description == "thick, windy"
    assert result.mass == 1.024e26

def test_get_by_planet_id_with_to_dict_method_returns_dict(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert type(response_body) == dict
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

#def test_from_dict_returns_book():
#     # Arrange
#     book_data = {
#         "title": "New Book",
#         "description": "The Best!"
#     }

#     # Act
#     new_book = Book.from_dict(book_data)

#     # Assert
#     assert new_book.title == "New Book"
#     assert new_book.description == "The Best!"

# def test_from_dict_with_no_title():
#     # Arrange
#     book_data = {
#         "description": "The Best!"
#     }

#     # Act & Assert
#     with pytest.raises(KeyError, match = 'title'):
#         new_book = Book.from_dict(book_data)

# def test_from_dict_with_no_description():
#     # Arrange
#     book_data = {
#         "title": "New Book"
#     }

#     # Act & Assert
#     with pytest.raises(KeyError, match = 'description'):
#         new_book = Book.from_dict(book_data)

# def test_from_dict_with_extra_keys():
#     # Arrange
#     book_data = {
#         "extra": "some stuff",
#         "title": "New Book",
#         "description": "The Best!",
#         "another": "last value"
#     }
    
#     # Act
#     new_book = Book.from_dict(book_data)

#     # Assert
#     assert new_book.title == "New Book"
#     assert new_book.description == "The Best!"
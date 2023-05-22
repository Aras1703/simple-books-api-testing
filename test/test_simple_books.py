import pytest
from endpoint.simple_books import SimpleBooksAPI

@pytest.fixture()
def simplebooks_api():
    return SimpleBooksAPI()


def test_get_status(simplebooks_api):
    response = simplebooks_api.get_status()
    assert response.status_code == 200
    
    
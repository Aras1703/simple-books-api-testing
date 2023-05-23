import pytest
import names
from endpoint.simple_books import SimpleBooksAPI

@pytest.fixture()
def simplebooks_api():
    return SimpleBooksAPI()
    

def test_get_status(simplebooks_api):
    response = simplebooks_api.get_status()
    assert response.status_code == 200

def test_get_list_books(simplebooks_api):
    response = simplebooks_api.get_list_books()
    assert response.status_code == 200

def test_get_single_book(simplebooks_api):
    bookId=5
    response = simplebooks_api.get_single_book(bookId)
    assert response.status_code == 200
    data = response.json()
    assert data['current-stock'] > 0

def test_post_order_book(simplebooks_api):
    #Register to get the api key
    Name = names.get_first_name(gender='male')
    Email = Name+'@gmail.com'
    api_key = simplebooks_api.regist_api_key(Name, Email)
    token = api_key.json().get('accessToken')

    response = simplebooks_api.order_book(bookId=5, 
                                          customerName='Bazw', 
                                          api_key=token,)
    assert response.status_code == 201
    
    
    
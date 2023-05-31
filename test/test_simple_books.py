import pytest
import names
from endpoint.simple_books import SimpleBooksAPI

@pytest.fixture(scope='session')
def simplebooks_api():
    return SimpleBooksAPI()

def get_api_key():
    # Create Instance
    api = SimpleBooksAPI()
    
    # Register to get the api key
    Name = names.get_first_name(gender='female')+'Nay'
    Email = Name+'@gmail.com'
    api_key = api.regist_api_key(Name, Email)
    return api_key.json().get('accessToken')
    

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
    assert data['available'] == True

def test_post_order_book(simplebooks_api):
    # Get api key
    token = get_api_key()
    response = simplebooks_api.order_book(bookId=5, 
                                          customerName='Bazw', 
                                          api_key=token)
    assert response.status_code == 201

def test_get_all_book_orders(simplebooks_api):
    token = get_api_key()
    response = simplebooks_api.get_all_book_orders(token)
    assert response.status_code == 200

def test_get_ordered_book(simplebooks_api):
    token = get_api_key()
    post_order_book = simplebooks_api.order_book(bookId=5, 
                                                customerName='Bazw', 
                                                api_key=token)
    
    orderId = post_order_book.json().get('orderId')
    response = simplebooks_api.get_ordered_book(orderId=orderId, api_key=token)
    assert response.status_code == 200
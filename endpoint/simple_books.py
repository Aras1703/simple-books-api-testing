from endpoint.base import APIClient

class SimpleBooksAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://simple-books-api.glitch.me'
    
    def get_status(self):
        return self.get(self.base_url+'/status')
    
    def regist_api_key(self, Name, Email):
        payload = {
            'clientName':Name,
            'clientEmail':Email,
        }
        return self.post(self.base_url+'/api-clients', data=payload)
    
    def get_list_books(self):
        return self.get(self.base_url+'/books')
    
    def get_single_book(self, booksId):
        return self.get(f'{self.base_url}/{booksId}')
    
    def order_book(self, bookId, customerName, api_key):
        payload = {
            'bookId':bookId,
            'customerName':customerName,
        }
        headers = {
            'Authorization':api_key,
        }
        return self.post(self.base_url+'/orders', data=payload, headers=headers)
    
    def get_all_book_orders(self, api_key):
        headers = {
            'Authorization':api_key,
        }
        return self.get(self.base_url+'/orders', headers=headers)
    
    def get_ordered_book(self, orderId, api_key):
        headers = {
            'Authorization':api_key,
        }
        return self.get(f'{self.base_url}/orders/:{orderId}', headers=headers)
    
    def update_order(self, orderId, customerName, api_key):
        headers = {
            'Authorization':api_key,
        }
        return self.patch(f'{self.base_url}/orders/:{orderId}', headers=headers, data=customerName)
    
    def delete_order(self, orderId, api_key):
        headers = {
            'Authorization':api_key,
        }
        return self.delete(f'{self.base_url}/orders/:{orderId}')
import requests


class BookUser:
    BOOKS = '/books'

    def __init__(self, base_url: str = 'http://127.0.0.1:5000'):
        self.base_url = base_url

    def get_all_books(self) -> requests.Response:
        return requests.get(f'{self.base_url}{self.BOOKS}')

    def post_book(self, title: str, author: str) -> requests.Response:
        request_body = {
            'title': title,
            'author': author,
        }
        return requests.post(f'{self.base_url}{self.BOOKS}', json=request_body)

    def delete_book_by_id(self, book_id: int) -> requests.Response:
        return requests.delete(f'{self.base_url}{self.BOOKS}/{book_id}')

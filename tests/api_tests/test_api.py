def test_post_book(book_client):
    response = book_client.post_book(
        title='Harry Potter and the Order of the Phoenix',
        author='J.K. Rowling'
    )
    assert response.status_code == 201

def test_get_books(book_client):
    response = book_client.get_all_books()
    assert response.status_code == 200

def test_delete_book(book_client):
    response = book_client.delete_book_by_id()
    assert response.status_code == 204

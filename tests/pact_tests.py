def test_get_user(book_client, books_pact):
    expected = [
        {
            'id': 1,
            'author': 'George Orwell',
            'title': '1984'
        },
    ]
    books_pact.given('Books 1, 2 exist').upon_receiving('Request for all books').with_request('get', '/books').will_respond_with(200, body=expected)

    with books_pact:
        response = book_client.get_all_books()
        assert response.json() == expected

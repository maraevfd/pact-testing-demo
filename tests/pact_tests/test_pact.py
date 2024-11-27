from pact.matchers import EachLike, Format, Term


def test_get_users(books_client, books_pact):
    expected = EachLike(
        {
            'id': Format().identifier,
            'author': Term(
                matcher=r'^[a-zA-Z0-9 ]+$',
                generate='George Orwell'
            ),
            'title': Term(
                matcher=r'^[a-zA-Z0-9 ]+$',
                generate='1984'
            )
        },
    )

    books_pact.given(
        'There are books available'
    ).upon_receiving(
        'a request for all books'
    ).with_request(
        'get', '/books'
    ).will_respond_with(
        status=200,
        body=expected,
    )

    with books_pact:
        response = books_client.get_all_books()
        for book in response.json():
            assert isinstance(book, dict), f"Item is not a dict: {book}"

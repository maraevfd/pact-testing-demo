from pact.matchers import EachLike, Format, Term, Like


def test_get_all_users(books_client, books_pact):
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
        body=Like(expected),
    )

    with books_pact:
        response = books_client.get_all_books()
        for book in response.json():
            assert isinstance(book, dict), f"Item is not a dict: {book}"


def test_post_user(books_client, books_pact):
    new_book = {
        'title': 'New Book',
        'author': 'John Doe'
    }

    expected = {
        'id': Format().identifier,
        'author': 'John Doe',
        'title': 'New Book'
    }

    books_pact.given(
        'The library accepts new books'
    ).upon_receiving(
        'a request to add a new book'
    ).with_request(
        method='post',
        path='/books',
        body=Like(new_book),
    ).will_respond_with(
        status=201,
        body=expected,
    )

    with books_pact:
        added_book = books_client.post_book(**new_book).json()
        assert isinstance(added_book, dict)

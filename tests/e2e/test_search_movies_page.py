# TODO: Feature 3 Done by Soren Wilson
from flask.testing import FlaskClient
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository


def test_search_movies():
    movie_repository.create_movie("1917", "Sam Mendes", "5")
    test_app = app.test_client()
    response = test_app.get('/movies/search', data={"movie_name": "1917"})
    response_data = response.data
    
    assert response.status_code == 200
    assert b'<th scope="col">Movie</th>' in response_data
    assert b'<td>5</td>' in response_data

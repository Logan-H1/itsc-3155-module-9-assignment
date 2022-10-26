# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository

#call create_movie() to create a certain movie
#then test to see if its in all movies

def test_all_movies_page():
    movie = movie_repository.create_movie("The Dark Knight", "Christopher Nolan", "4")
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<td>The Dark Knight</td>' in response.data
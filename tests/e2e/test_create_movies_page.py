# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository
import pytest
from src.models.movie import Movie

@pytest.fixture()
def test_app():
  return app.test_client()


def test_movie_created_end(test_app):
    response = test_app.post('/movies', data={
        "movie_name": "The Dark Knight",
        "director_name": "Christopher Nolan",
        "movie_rating": 5
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"The Dark Knight" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"5" in response.data
    
    test_movie = Movie("The Dark Knight", "Christopher Nolan", 5)
    all_movies = movie_repository.get_all_movies()
    print(test_movie.__dict__)

    same_movie = False

    for movie in all_movies:
        if movie.__dict__ == test_movie.__dict__:
            same_movie = True
    
    assert same_movie
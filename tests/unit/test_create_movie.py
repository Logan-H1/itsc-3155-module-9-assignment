# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from app import app

def test_movie_created():
    test_app = app.test_client()
    response = test_app.post('/movies')
    assert r esponse.status_code == 200


"""     test_app = app.test_client()
    movie_name = "The Dark Knight"
    director_name = "Christopher Nolan"
    movie_rating = 5
    test_movie = create_movie(movie_name, director_name_ movie_rating)
    data={
        "movie_name": "Dark Knight",
        "director_name": "CN",
        "movie_rating": "4"
    }
    response = test_app.post('/movies', json = data )
    movies = get_all_movies() 
    assert test_movie in movies """
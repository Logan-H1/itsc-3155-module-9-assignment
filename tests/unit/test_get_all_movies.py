# TODO: Feature 1
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository

#add key and value directly to dictionary
#assert if said key and value are in dictionary

def test_get_all_movies():
    movie = Movie('Star Wars', 'George Lucas', 5)

    movie_repository.get_all_movies()

    assert type(movie) == Movie
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5

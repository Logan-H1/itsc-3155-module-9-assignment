# TODO: Feature 3 Done by Soren Wilson
from src.models.movie import Movie
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

import pytest


def test_get_movie_by_title():
    check_rating = "5"
    movie_repository.create_movie("1917", "Sam Mendes", "5")
    by_title = movie_repository.get_movie_by_title("1917")
    
    same_rating = False

    if(by_title.rating == check_rating):
        same_rating = True

    assert same_rating

def test_get_movie_by_title():
    check_rating = "5"
    movie_repository.create_movie("1917", "Sam Mendes", "5")
    by_title = movie_repository.get_movie_by_title("Hacksaw Ridge")
    
    same_rating = False
    
    if(by_title.rating == check_rating):
        same_rating = True

    assert not same_rating

def test_get_movie_by_title():
    check_rating = "5"
    movie_repository.create_movie("1917", "Sam Mendes", "5")
    by_title = movie_repository.get_movie_by_title("1917")
    
    same_rating = False
    
    if(by_title.rating == "4"):
        same_rating = True

    assert not same_rating
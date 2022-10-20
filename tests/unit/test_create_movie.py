# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository


def test_movie_created():
    mov = get_movie_repository()
    assert len(mov) == 1
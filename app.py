from flask import Flask, redirect, render_template, request
from src.models.movie import Movie

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movie = request.form.get('move_name', type=str)
    rating = request.form.get('rating', type=int)

    movie_rating = {}
    movie_rating[movie] = rating
    if movie_rating == ():
        return render_template('no_movies_listed.html')

    return render_template('list_all_movies.html', movie_rating=movie_rating)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    movie_name = request.form.get('movie_name', type = str)
    movie_director = request.form.get('director_name', type = str)
    movie_rating = request.form.get('movie_rating', type = int)
    movie_repository.create_movie(movie_name, movie_director, movie_rating)
    
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

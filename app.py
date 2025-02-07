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
    
    movies = movie_repository.get_all_movies()
    
    return render_template('list_all_movies.html', movies=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    movie_name = request.form.get('movie_name', type = str)
    movie_director = request.form.get('director_name', type = str)
    movie_rating = request.form.get('movie_rating', type = int)
    movie_repository.create_movie(movie_name, movie_director, movie_rating)

    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search', methods=["GET", "POST"])
def search_movies():
    # TODO: Feature 3
    movie_name = request.form.get('movie_name', type = str)
    movie_title = movie_repository.get_movie_by_title(movie_name)
    return render_template('search_movies.html', search_active=True, movie_title=movie_title)

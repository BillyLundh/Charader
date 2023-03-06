import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

movies = [
    {"name": "Vito Corleone", "rating": "The Godfather"},
    {"name": "Marty McFly", "rating": "Back to the future"},
    {"name": "Darth Vader", "rating": "Star Wars"},
    {"name": "John McClain", "rating": "Die Hard"},
    {"name": "Derek Zoolander", "rating": "Zoolander"},
    {"name": "Forrest Gump", "rating": "Forrest Gump"}
]

def get_random_movie():
    return random.choice(movies)

@app.route('/')
def home():
    return render_template("index.html", movies=movies)

# Hello world!

@app.route('/info')
def info():
    # ?movie=2
    movie_index = int(request.args["movie"])
    return render_template("info.html",
                           name=movies[movie_index]["name"],
                           rating=movies[movie_index]["rating"])


@app.route('/remove/<int:movie>', methods=["GET"])
def remove(movie):
    movies.pop(movie)
    return redirect('/')


@app.route('/add', methods=["POST"])
def add():
    movie_name = request.form["name"]
    movie_rating = request.form["rating"]
    new_movie = {"name": movie_name, "rating": movie_rating}
    movies.append(new_movie)
    return redirect('/')


@app.route('/random')
def random_movie():
    movie = get_random_movie()
    return render_template("info.html",
                           name=movie["name"],
                           rating=movie["rating"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2000, debug=True)

from fastapi.testclient import TestClient
from app.src.movies_api import app

client = TestClient(app)


def test_create_movie1():
    movie = {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "genre": "Crime"
    }
    response = client.post("/movies", json=movie)
    assert response.status_code == 200
    assert response.json()["title"] == "The Godfather"


def test_create_movie2():
    movie = {
        "title": "The Godfather Part II",
        "director": "Francis Ford Coppola",
        "year": 1974,
        "genre": "Crime"
    }
    response = client.post("/movies", json=movie)
    assert response.status_code == 200
    assert response.json()["genre"] == "Crime"


def test_read_movie():
    movie_title = "The Godfather"
    response = client.get(f"/movies/title/{movie_title}")
    assert response.status_code == 200
    assert response.json()["title"] == "The Godfather"


def test_read_movie_should_fail():
    movie_title = "Avengers: Endgame"
    response = client.get(f"/movies/title/{movie_title}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_update_movie():
    movie_id = "642e2115c1e8eae96f9ee7c1"
    updated_movie = {
        "title": "The Godfather Part II",
        "director": "Francis Ford Coppola",
        "year": 1974
    }
    response = client.put(f"/movies/{movie_id}", json=updated_movie)
    assert response.status_code == 200
    assert response.json() == {"message": "Movie updated successfully"}


def test_delete_movie():
    movie_id = client.get(f"/movies/title/The Godfather Part II").json()["_id"]["$oid"]
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Movie deleted successfully"}


def test_delete_movie_should_fail():
    movie_id = "000"
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}

def test_read_all_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    assert len(response.json()) > 0

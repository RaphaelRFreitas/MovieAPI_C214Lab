from bson.objectid import ObjectId
from pymongo import MongoClient
from fastapi.testclient import TestClient
from app.src.movies_api import app

APIclient = TestClient(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["test_movies"]
collection = db["test_collection"]
collection.delete_many({})

#Testa se o banco de dados está vazio
def test_database_is_empty():
    assert collection.count_documents({}) == 0

# Testa a criação de um novo filme
def test_create_movie():
    movie = {'title':"The Godfather",
             'director':"Francis Ford Coppola",
             'year':1972,
             'genre':"Crime"}
    response = APIclient.post("/movies/", json=movie)
    assert response.status_code == 200
    assert response.json()["title"] == "The Godfather"

# Testa a leitura de todos os filmes
def test_read_movies():
    response = APIclient.get("/movies/")
    assert response.status_code == 200
    assert len(response.json()) > 0


# Testa a leitura de um filme específico pelo título
def test_read_movie_by_title():
    movie_title = "The Godfather"
    response = APIclient.get(f"/movies/title/{movie_title}")
    assert response.status_code == 200
    assert response.json()["title"] == "The Godfather"

# Testa a atualização de um filme específico pelo titulo
def test_update_movie():
    movie_title = "The Godfather"
    updated_movie = {"title": "The Godfather Part II", "director": "Francis Ford Coppola", "year": 1974, 'genre':"Drama"}
    response = APIclient.put(f"/movies/{movie_title}", json=updated_movie)
    assert response.status_code == 200
    assert response.json()["message"] == "Movie updated successfully"

# Testa a deleção de um filme específico pelo titulo
def test_delete_movie():
    movie_title = "The Godfather Part II"
    response = APIclient.delete(f"/movies/title/{movie_title}")
    assert response.status_code == 200
    assert response.json()["message"] == "Movie deleted successfully"

# Testa a leitura de um filme inexistente pelo ID
def test_read_nonexistent_movie_by_id():
    nonexistent_movie_id = str(ObjectId())
    response = APIclient.get(f"/movies/{nonexistent_movie_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Movie not found"

# Testa a deleção de um filme inexistente pelo ID
def test_delete_nonexistent_movie():
    nonexistent_movie_id = str(ObjectId())
    response = APIclient.delete(f"/movies/{nonexistent_movie_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Movie not found"
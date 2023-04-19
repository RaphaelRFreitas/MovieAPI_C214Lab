from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
from app.src.Movie.movie import Movie
import json

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["movies"]
collection = db["movies"]

# Cria um novo filme
@app.post("/movies/")
async def create_movie(movie: Movie):
    result = collection.insert_one(movie.dict())
    return {**movie.dict(), "id": str(result.inserted_id)}

# Retorna todos os filmes
@app.get("/movies/")
async def read_movies():
    movies = collection.find()
    return json.loads(json_util.dumps(movies))

# Retorna um filme específico pelo ID
@app.get("/movies/{movie_id}")
async def read_movie(movie_id: str):
    movie = collection.find_one({"_id": ObjectId(movie_id)})
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return json.loads(json_util.dumps(movie))

# Retorna um filme específico pelo título
@app.get("/movies/title/{movie_title}")
async def read_movie(movie_title: str):
    movie = collection.find_one({"title": movie_title})
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return json.loads(json_util.dumps(movie))

# Atualiza um filme específico pelo ID
@app.put("/movies/{movie_id}")
async def update_movie(movie_id: str, movie: Movie):
    result = collection.update_one({"_id": ObjectId(movie_id)}, {"$set": movie.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie updated successfully"}

# Deleta um filme específico pelo ID
@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: str):
    result = collection.delete_one({"_id": ObjectId(movie_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}

# Movies API
This is a simple movies API built using FastAPI and MongoDB. The API allows you to create, read, update, and delete (CRUD) movie information in a MongoDB database.

## Installation
To install the necessary dependencies, run the following command in the terminal:

```bash
pip install fastapi pymongo uvicorn
```
## Running the API
To start the API server, run the following command in the terminal:

```bash
uvicorn app.src.movies_api:app --reload
```
This will start the API server on port 8000.

## Testing the API
You can test the API using a tool like Postman or by using the command line with the curl utility. Here are some examples of how to test each CRUD operation:

## Creating a movie
To create a new movie, make a POST request to the **/movies** endpoint with the following JSON payload:

```json
{
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1972
}
```
For example, using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972}' http://localhost:8000/movies
```
## Reading a movie
To read information about a specific movie, make a GET request to the **/movies/{movie_id}** endpoint, where **{movie_id}** is the ID of the movie you want to query.

For example, using curl:

```bash
curl http://localhost:8000/movies/6167f2e74f5db4222c7985e5
```
## Updating a movie
To update information about a movie, make a PUT request to the **/movies/{movie_id}** endpoint, where **{movie_id}** is the ID of the movie you want to update. Include the JSON payload with the updated movie information.

For example, using curl:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title": "The Godfather Part II", "director": "Francis Ford Coppola", "year": 1974}' http://localhost:8000/movies/6167f2e74f5db4222c7985e5
```
## Deleting a movie
To delete a movie, make a DELETE request to the /movies/{movie_id} endpoint, where {movie_id} is the ID of the movie you want to delete.

For example, using curl:

```bash
curl -X DELETE http://localhost:8000/movies/6167f2e74f5db4222c7985e5
```
## Conclusion
With these basic instructions, you should be ready to start using the movies API. Remember that you can customize the API and add additional features, such as user authentication and input validation, as needed.
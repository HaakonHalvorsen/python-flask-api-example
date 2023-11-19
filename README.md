## How to run API locally with Docker
1.  `docker build -t IMAGE_NAME .`: Builds Docker image.
2. 
- WINDOWS: `docker run -dp 5000:5000 -w /app -v "/c/LOCAL_PATH_TO_PROJECT_FOLDER/flask-workshop:/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"`: Run Docker container with hot reloading.
- LINUX: `docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"`: Run Docker container with hot reloading.
3. API should work! Use Postman to test. Go to http://127.0.0.1:5000/swagger-ui to check Swagger documentation.

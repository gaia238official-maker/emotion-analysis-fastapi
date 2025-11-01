# Emotion Analysis FastAPI

This repository contains a minimal FastAPI application with SQLite integration for storing and retrieving emotion analysis results. It includes a simple test endpoint for health checks and can be containerized using Docker and run with docker-compose.

## Features

- Uses FastAPI to provide RESTful endpoints.
- SQLite database via SQLAlchemy for persistence.
- Dockerfile to containerize the application.
- docker-compose.yml for easy local development.
- Test endpoint (`/test`) to verify the API is running.

## Getting Started

### Running locally

1. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

2. Start the server with Uvicorn:

```bash
uvicorn main:app --reload
```

3. The API will be available at `http://localhost:8000`. You can access interactive API docs at `http://localhost:8000/docs`.

### Using Docker

1. Build the Docker image:

```bash
docker build -t emotion-analysis-fastapi .
```

2. Run the container:

```bash
docker run -p 8000:8000 emotion-analysis-fastapi
```

### Using docker-compose

1. Ensure Docker and docker-compose are installed.

2. Start the services:

```bash
docker-compose up --build
```

3. This will build the image (if necessary) and run the API. The service exposes port 8000 on your local machine.

### Test endpoint

To verify the API is running, request the `/test` endpoint:

```bash
curl http://localhost:8000/test
```

You should receive a JSON response like:

```json
{"message": "API is up and running"}
```

# Emotion Analysis FastAPI

This repository contains a minimal FastAPI application with SQLite integration for storing and retrieving emotion analysis results.

## Features

- Uses FastAPI to provide RESTful endpoints.  
- SQLite database via SQLAlchemy for persistence.  
- Dockerfile to containerize the application.

## Getting Started

### Running locally

1. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

2. Start the server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### Using Docker

Build and run the Docker container:

```bash
docker build -t emotion-analysis .
docker run -p 8000:8000 emotion-analysis
```

Then access the API at `http://localhost:8000`.

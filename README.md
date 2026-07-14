# FastAPI + PostgreSQL: Secure User Model & CI/CD

A FastAPI application with a SQLAlchemy-backed user model, Pydantic validation,
bcrypt password hashing, and a full CI/CD pipeline that tests against a real
Postgres instance and pushes a Docker image to Docker Hub on success.

## Docker Hub


    docker pull mj464/fastapi-user-model:latest

## Project Structure

    .
    main.py              # FastAPI app entrypoint
    database.py          # SQLAlchemy engine/session setup
    models.py             # User SQLAlchemy model
    schemas.py            # UserCreate / UserRead Pydantic schemas
    security.py            # Password hashing (bcrypt via passlib)
    docker-compose.yml     # Local Postgres + pgAdmin + app stack
    Dockerfile             # Image definition for the app
    requirements.txt
    tests/
        conftest.py                 # DB fixture for integration tests
        test_security.py            # Unit tests: hashing
        test_schemas.py             # Unit tests: Pydantic validation
        test_user_integration.py    # Integration tests: real Postgres

## Running Tests Locally

1. Create a virtual environment and install dependencies:

       python -m venv venv
       source venv/Scripts/activate   # Windows Git Bash
       pip install -r requirements.txt

2. Start a local Postgres instance:

       docker-compose up -d db

3. Run the full test suite:

       pytest tests/ -v

   Unit tests (`test_security.py`, `test_schemas.py`) don't require a database.
   Integration tests (`test_user_integration.py`) connect to Postgres using the
   `TEST_DATABASE_URL` environment variable, defaulting to
   `postgresql://postgres:postgres@localhost:5432/fastapi_db`.

## CI/CD Pipeline

On every push to `main`/`master`:

1. **Test job** — spins up a disposable Postgres service container in GitHub
   Actions, installs dependencies, and runs the full test suite.
2. **Build & push job** — only runs if all tests pass. Builds the Docker image
   from the `Dockerfile` and pushes it to Docker Hub as
   `mj464/fastapi-user-model:latest`.


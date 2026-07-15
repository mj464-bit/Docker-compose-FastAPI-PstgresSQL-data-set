FastAPI + PostgreSQL: Secure User Model, Calculations and CI/CD

A FastAPI application with SQLAlchemy models for users and calculations, Pydantic validation, bcrypt password hashing, a factory pattern for calculation logic, and a full CI/CD pipeline that tests against a real Postgres instance and pushes a Docker image to Docker Hub on success.

Docker Hub

Image: mj464/fastapi-user-model
https://hub.docker.com/r/mj464/fastapi-user-model

Pull command:
docker pull mj464/fastapi-user-model:latest

Project Structure

main.py               FastAPI app entrypoint
database.py            SQLAlchemy engine and session setup
models.py               User and Calculation SQLAlchemy models
schemas.py               Pydantic schemas for User and Calculation
security.py               Password hashing using bcrypt via passlib
calculation_factory.py     Factory pattern for Add, Sub, Multiply, Divide
docker compose.yml         Local Postgres, pgAdmin and app stack
Dockerfile                  Image definition for the app
requirements.txt

tests folder contains:
conftest.py                        Database fixture for integration tests
test_security.py                    Unit tests for hashing
test_schemas.py                      Unit tests for User schema validation
test_user_integration.py              Integration tests for User and Postgres
test_calculation_factory.py            Unit tests for factory operation logic
test_calculation_schemas.py             Unit tests for Calculation schema validation
test_calculation_integration.py          Integration tests for Calculation and Postgres

Models

User table app_users contains username, email, password_hash and created_at. Unique constraints on username and email.

Calculation table app_calculations contains a, b, type as an enum with values Add, Sub, Multiply and Divide, result, and an optional user_id foreign key to app_users.id.

Table names are prefixed with app to avoid colliding with the raw SQL tables from an earlier module running against the same database.

Running Tests Locally

Step one, create a virtual environment and install dependencies.
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

Step two, start a local Postgres instance.
docker compose up -d db

Step three, run the full test suite.
pytest tests/ -v

Unit tests do not require a database. These are test_security.py, test_schemas.py, test_calculation_factory.py and test_calculation_schemas.py.

Integration tests connect to Postgres using the environment variable TEST_DATABASE_URL, defaulting to postgresql://postgres:postgres@localhost:5432/fastapi_db. These are test_user_integration.py and test_calculation_integration.py.

CI/CD Pipeline

On every push to main or master, two jobs run.

Test job spins up a disposable Postgres service container in GitHub Actions, installs dependencies and runs the full test suite, covering both user and calculation tests together.

Build and push job only runs if all tests pass. It builds the Docker image from the Dockerfile and pushes it to Docker Hub as mj464/fastapi-user-model:latest.

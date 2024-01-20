# FastAPI Docker Template Repository

A template docker-compose setup for a FastAPI instance, powered by a PostgresSQL database and connected with SQLAlchemy and Pydantic.
In addition, there is a basic test suite with 100% code coverage using pytest.

# Project Structure

```
├── .dockerignore
├── .gitignore
├── .vscode
│   ├── extensions.json
│   └── settings.json
├── Makefile
├── README.md
├── api
│   ├── db
│   │   ├── base.py
│   │   ├── engine.py
│   │   └── user.py
│   ├── main.py
│   ├── schemas
│   │   └── user.py
│   └── tests
│       ├── conftest.py
│       └── integration
│           └── ...
├── db
│   └── init.sql
├── docker
│   └── api
│       ├── Dockerfile
│       ├── requirements-dev.txt
│       └── requirements.txt
├── docker-compose.yml
└── ruff.toml
```

# User Guide

The commands in the Makefile should be enough to get you started in running the FastAPI and database locally, as well as running linting, formatting and tests.

## Bringing up the API and DB

This will bring up the API and create a Postrges instance. The API will only come up when the Postgres container has passed its healthcheck.
```bash
make run
```

## Running Tests

Run pytest against the API.
```bash
make test
```

### Generate Test Coverage Report

```bash
make coverage
```

## Ruff

This project uses Ruff as the linter and formatter to keep the code formatted. Run the linter and formatter either locally or through the `api` container.

### Run Linter

To run locally:
```bash
make lint
```

To run through the container:
```bash
make lint-api
```

### Run Formatter

To run locally:
```bash
make format
```

To run through the container:
```bash
make format-api
```

### Run Both Linter and Formatter

To run locally:
```bash
make lf
```

To run through the container:
```bash
make lf-api
```
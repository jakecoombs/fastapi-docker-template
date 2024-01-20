PYTHON=python3.11

.PHONY: lint-api
lint-api:
	docker compose run --rm api ${PYTHON} -m ruff check --fix .

.PHONY: format-api
format-api:
	docker compose run --rm api ${PYTHON} -m ruff format .

.PHONY: lf-api
lf-api:
	docker compose run --rm api \
		${PYTHON} -m ruff check --fix . &&\
		${PYTHON} -m ruff format .

.PHONY: lint
lint:
	${PYTHON} -m ruff check --fix api

.PHONY: format
format:
	${PYTHON} -m ruff format api

.PHONY: lf
lf: lint format

.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up -d

.PHONY: pytest-coverage
pytest-coverage:
	docker compose run --rm api coverage run -m pytest tests

.PHONY: test
test:
	docker compose run --rm api ${PYTHON} -m pytest tests

.PHONY: coverage
coverage: pytest-coverage
	docker compose run --rm api coverage report -m

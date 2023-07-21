VENV                := .venv
VENV_PYTHON         := $(VENV)/bin/python

SYSTEM_PYTHON       := $(or $(shell which python3), $(shell which python))
PYTHON              := $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
POETRY              := $(shell command -v poetry 2> /dev/null)

PRE_COMMIT          := pre-commit

DOCKER_COMPOSE_FILE := docker-compose.yaml

.PHONY: black lint isort

black:
	$(POETRY) run black . $(args)

lint:
	$(POETRY) run flake8 $(args)

isort:
	$(POETRY) run isort . $(args)

.PHONY: test

test:
	$(POETRY) run pytest

.PHONY: run

run:
	@echo 'Running app'
	$(POETRY) run $(PYTHON) manage.py runserver

.PHONY: autoupdate all-files

autoupdate:
	$(PRE_COMMIT) autoupdate

all-files:
	$(PRE_COMMIT) run --all-files

.PHONY: build run-app stop clean

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) build

run-app:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

stop:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

clean:
	docker system prune -af --volumes
	docker network prune -f

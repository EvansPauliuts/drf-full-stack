VENV                := .venv
VENV_PYTHON         := $(VENV)/bin/python

SYSTEM_PYTHON       := $(or $(shell which python3), $(shell which python))
PYTHON              := $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
POETRY              := $(shell command -v poetry 2> /dev/null)

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
	pre-commit autoupdate

all-files:
	pre-commit run --all-files

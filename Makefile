SHELL=C:/Windows/System32/cmd.exe
ENV = env
PYBIN = $(ENV)/scripts
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip
PYTEST = $(PYTHON) -m pytest
COVERAGE = $(PYTHON) -m coverage
PYFLAKE8 = $(PYTHON) -m flake8
TESTDIR = tests

environ: clean requirements-dev.txt
	virtualenv $(ENV)
	$(PIP) install -r requirements-dev.txt
	@echo "initialization complete"

.PHONY: help
help:
	@echo "make                      # create virtual env and setup dependencies"
	@echo "make tests                # run tests"
	@echo "make coverage             # run tests with coverage report"
	@echo "make lint                 # check linting"
	@echo "make flake8               # alias for `make lint`"
	@echo "make clean                # remove more or less everything created by make"

.PHONY: tests
tests:
	$(PYTEST) $(TESTDIR) -vv

.PHONY: coverage
coverage:
	$(PYTEST) $(TESTDIR) -vv --cov=work_classes
	$(COVERAGE) html
	
.PHONY: lint
lint:
	$(PYFLAKE8)
	
.PHONY: flake8
flake8:
	$(PYFLAKE8)

.PHONY: clean
clean:
	if exist $(ENV) rd $(ENV) /q /s
	if exist .coverage del .coverage
	if exist htmlcov rd htmlcov /q /s
	del /S *.pyc
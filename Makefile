# Makefile with all options required for develop and running this software

VENV=.venv
PYTHON=${VENV}/bin/python3
MAKE=make

.DEFAULT: help

help:
	@echo "make setup -> Setups virtual environment and install deps."
	@echo "make clean -> Cleans environment."
	@echo "make refresh -> Install new dependencies."
	@echo "make format -> Runs code format using Black."
	@echo "make format-test -> Check Black standard code compliance."
	@echo "make unit-test -> Runs unit tests."
	@echo "make full-test -> Runs full test (unit & format)."


setup:
	@echo "Setting up a virtual environment ..."
	if test -d ${VENV}; then true; else python3.8 -m venv ${VENV}; fi
	${PYTHON} -m pip install -U pip==22.3.1
	${MAKE} refresh

clean:
	rm -rf ${VENV} .pytest_cache .coverage

refresh:
	${PYTHON} -m pip install -r requirements.txt

format:
	${PYTHON} -m black code tests

format-test:
	${PYTHON} -m black --check code tests

unit-test:
	${PYTHON} -m pytest --cov=code --cov-config=.coveragerc tests

full-test: setup unit-test format-test

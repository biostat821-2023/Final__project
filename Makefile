PYTHON_FILES := $(shell git ls-files '*.py')

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black --diff --check $(PYTHON_FILES) &&\
	pycodestyle $(PYTHON_FILES) &&\
    pydocstyle $(PYTHON_FILES) &&\
	mypy $(PYTHON_FILES)

lint:
	pylint --disable=R,C $(PYTHON_FILES)

test:
	python -m pytest -vv tests
	
all: install format lint
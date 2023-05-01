install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black --diff --check $(git ls-files '*.py')
	pycodestyle $(git ls-files '*.py')
    pydocstyle $(git ls-files '*.py')
	mypy $(git ls-files '*.py')

lint:
	pylint --disable=R,C *.py

all: install format lint
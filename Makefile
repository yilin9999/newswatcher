#!make
.PHONY: venv
include ./.env
export

# make headline colorful
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

venv:
	@echo $(TAG)Generate python 3.7.4 virtualenv$(END)
	pip3 install virtualenv==16.7.9 --user
	pyenv local 3.7.4
	virtualenv --python=python --no-site-packages venv
	venv/bin/pip install --upgrade pip setuptools wheel
	venv/bin/pip install -r requirements.txt

poetry-env:
	pyenv local 3.7.4
	poetry install
	ln -sf $(shell poetry env info -p) venv

run:
	poetry run python app.py'
	# sh -c ' . venv/bin/activate ; python3 app.py'

docker-up:
	cd docker && docker-compose up -d

docker-down:
	cd docker && docker-compose down

test:
	@echo $(TAG)Running tests$(END)
	poetry run pytest -v tests
	# sh -c ' . venv/bin/activate ; pytest -v tests'

test_debug:
	@echo $(TAG)Running tests in the debug level$(END)
	poetry run pytest -v tests --log-cli-level=DEBUG
	# sh -c ' . venv/bin/activate ; pytest -v tests --log-cli-level=DEBUG'

lint:
	@echo $(TAG)Running Lint$(END)
	poetry run flake8 newswatcher --count --ignore=E501,E126
	# sh -c ' . venv/bin/activate ; flake8 oss --count --ignore=E501,E126'

flask_run:
	poetry run flask run
	# sh -c ' . venv/bin/activate ; flask run'
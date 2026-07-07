ci:	python -m pytest tests/

docker:	docker-compose up -d

develop:	pip install -e .

docs:	pip install -r docs/requirements.txt && mkdocs build

test:	$(ci)

lint:	black . && flake8 . && isort .

format:	black . && isort .
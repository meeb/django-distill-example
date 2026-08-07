all: clean build


full: setup clean build


setup:
	pipx install uv
	uv sync


build:
	mkdir -p docs
	mkdir -p media
	mkdir -p static
	uv run python3 manage.py collectstatic --noinput
	uv run python3 manage.py distill generate --force --output-directory=docs
	cp -av media docs/media


clean:
	rm -rf docs
	rm -rf static


lint:
	uvx ruff check


format:
	uvx ruff format


runserver:
	uv run manage.py migrate
	uv run manage.py runserver

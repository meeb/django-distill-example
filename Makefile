python=/usr/bin/env python

all: clean build

build:
	mkdir -p docs
	mkdir -p static
	$(python) manage.py collectstatic --noinput
	$(python) manage.py distill-local --force docs

clean:
	rm -rf docs
	rm -rf static

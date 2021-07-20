run:
  docker run -dp 4000:4000 python-webserver

build:
  docker build -t python-webserver .

req:
  pipenv lock --keep-outdated --requirements > requirements.txt

fmt:
  yapf --in-place --recursive **/*.py

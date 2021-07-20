FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update -y && \
    apt-get install -y python3.8 python3-pip python3.8-dev && \
    pip3 install pipenv

# Set the current working directory
WORKDIR /app

# Copy over the dependencies file
COPY Pipfile Pipfile.lock .

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

COPY src/ .

CMD ["pipenv", "run", "python3", "."]

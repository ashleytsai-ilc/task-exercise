FROM --platform=linux/amd64 python:3.9.7

ENV FLASK_APP=main

WORKDIR /task-exercise

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --keep-outdated

COPY . .

EXPOSE 8080

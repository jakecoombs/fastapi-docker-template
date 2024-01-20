FROM python:3.11-slim

WORKDIR /api

COPY ./requirements-dev.txt /api/requirements-dev.txt
COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements-dev.txt

COPY . /api
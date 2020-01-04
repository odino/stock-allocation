FROM python:3-alpine

RUN pip install pyyaml
COPY . /src
WORKDIR /src
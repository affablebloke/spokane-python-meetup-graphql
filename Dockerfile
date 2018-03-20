FROM python:3.6.4-alpine3.7

RUN apk add --update alpine-sdk libxml2-dev libxslt-dev python-dev postgresql-dev

RUN pip install --upgrade pip

RUN mkdir -p \
        /src/python \
        /code

WORKDIR /code

COPY ./demo/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --src=/src/python -r /code/requirements.txt

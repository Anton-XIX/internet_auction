FROM python:3.8-alpine

WORKDIR /usr/src/app


RUN pip install --upgrade pip

RUN apk update && apk add postgresql-dev python3-dev cargo libffi-dev \
                          openssl-dev musl-dev jpeg-dev zlib-dev libmagic gcc && \
                          pip install --no-cache-dir poetry==1.1.6

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]



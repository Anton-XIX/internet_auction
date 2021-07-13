FROM python:3.8

ENV HOME=/app
ENV APP_HOME=/app/web/

WORKDIR $APP_HOME

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -yyq netcat

RUN pip install --no-cache-dir poetry==1.1.6

COPY poetry.lock pyproject.toml $APP_HOME/

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY entrypoint.sh $APP_HOME

COPY . $APP_HOME

ENTRYPOINT ["/app/web/entrypoint.sh"]



FROM python:3.7

WORKDIR /usr/src/app
COPY pyproject.toml poetry.lock /usr/src/app/

ARG production

ENV YOUR_ENV=${YOUR_ENV} \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=0.12.17

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Project initialization:
RUN poetry config settings.virtualenvs.create false && \
    poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

CMD /bin/bash
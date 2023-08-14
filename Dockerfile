# pull official base image
FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /code

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y curl libpq-dev gcc python3-cffi git binutils libproj-dev gdal-bin locales locales-all wget ghostscript wkhtmltopdf && \
    apt-get clean autoclean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /var/cache/apt/archives/*.deb && \
    find /var/lib/apt -type f | xargs rm -f && \
    find /var/cache -type f -exec rm -rf {} \; && \
    find /var/log -type f | while read f; do echo -ne '' > $f; done;

# install dependencies
RUN pip install --upgrade pip && \
    pip install poetry && \
    pip install psycopg2 && \
    pip install gunicorn==20.1.0 gevent==21.12.0

COPY ./poetry.lock /code/
COPY ./pyproject.toml /code/

RUN strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5

RUN poetry config virtualenvs.create false --local && \
    poetry install

COPY ./ /code/

ENV GUNICORN_BIND  0.0.0.0:8000
ENV GUNICORN_TIMEOUT 60
ENV GUNICORN_WORKERS 2
ENV GUNICORN_THREADS 2

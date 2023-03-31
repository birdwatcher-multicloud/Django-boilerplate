FROM python:3.9-alpine3.17
LABEL maintainer="birdwatcher.multicloud@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

# Set up packages required for mariadb or python
RUN apk add --update --no-cache mariadb-connector-c-dev \
    && apk add --no-cache --virtual .build-deps \
    mariadb-dev \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    && pip install mysqlclient==1.4.2.post1 \
    && apk del .build-deps \
    && apk add libffi-dev openssl-dev libgcc 

# python dependencies
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home user

# For static files
RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R user:user /vol && \
    chmod -R 755 /vol

USER user
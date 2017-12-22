FROM alpine

RUN mkdir -p /unmade/phonebook/backend

WORKDIR /unmade/phonebook/backend
COPY ./backend/requirements /unmade/phonebook/backend/requirements

RUN apk update && \
    apk upgrade && \
    apk add --update python3 python3-dev git postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements/local.txt && \
    apk del -r python3-dev postgresql git

WORKDIR /unmade/phonebook/web/backend/phonebook
FROM alpine

RUN addgroup -S phonebook && \
    adduser -S -g phonebook phonebook && \
    mkdir -p /home/phonebook/backend

WORKDIR /home/phonebook/backend
COPY ./backend/requirements /home/phonebook/backend/requirements

RUN apk update && \
    apk upgrade && \
    apk add --update python3 python3-dev git postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements/local.txt && \
    apk del -r python3-dev postgresql git && \
    mkdir -p phonebook/static/admin && \
    chown -R phonebook:phonebook /home/phonebook/backend

WORKDIR /home/phonebook/backend/phonebook
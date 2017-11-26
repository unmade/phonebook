FROM alpine

RUN addgroup -S phonebook && \
    adduser -S -g phonebook phonebook && \
    mkdir -p /home/phonebook/backend

WORKDIR /home/phonebook/backend
COPY ./requirements /home/phonebook/backend/requirements

RUN apk update && \
    apk upgrade && \
    apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements/prod.txt && \
    apk del -r python3-dev postgresql && \
    mkdir -p phonebook/static/admin && \
    chown -R phonebook:phonebook /home/phonebook/backend

COPY . /home/phonebook/backend
WORKDIR /home/phonebook/backend/phonebook
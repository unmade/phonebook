FROM alpine

RUN apk update && \
    apk upgrade && \
    apk add --update python3 python3-dev git postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev

COPY ./backend/requirements /requirements
RUN pip3 install --upgrade pip && \
    pip3 install -r /requirements/prod.txt && \
    pip3 install -r /requirements/test.txt && \
    apk del -r python3-dev postgresql git

COPY ./compose/web/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./compose/web/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]

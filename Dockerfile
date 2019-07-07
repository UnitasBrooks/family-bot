FROM alpine:latest
RUN apk add --no-cache py3-pip python3-dev gcc
RUN apk add bash
RUN mkdir -p /app
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY family_bot.py /app/

ENTRYPOINT /app/family_bot.py

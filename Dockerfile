FROM alpine:latest
RUN apk add --no-cache py3-pip python3-dev gcc
RUN mkdir -p /app
COPY family_bot.py requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT /app/family_bot.py

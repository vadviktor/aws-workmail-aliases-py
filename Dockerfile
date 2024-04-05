FROM python:3.12.2-alpine3.18

ENV FLASK_ENV=production

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

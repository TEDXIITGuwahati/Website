# syntax=docker/dockerfile:1.4

FROM python:3.7-alpine AS builder
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg
EXPOSE 8000
WORKDIR /app 
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir \
    && apk del build-deps
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

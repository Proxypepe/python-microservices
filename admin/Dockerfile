FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

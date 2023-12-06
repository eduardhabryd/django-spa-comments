FROM python:3.11.4-slim

LABEL maintainer="eduardhabryd@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip install psycopg2

RUN pip install -r requirements.txt

RUN adduser --disabled-password --no-create-home django-user
USER django-user

CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata fixture.json && python manage.py runserver 0.0.0.0:8000"]

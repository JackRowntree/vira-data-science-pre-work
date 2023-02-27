FROM python:3.8.3-slim-buster
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000
CMD python app.py
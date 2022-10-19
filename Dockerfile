FROM python:3.9.6

WORKDIR /click2call

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./bootstrap-5.2.0-dist ./bootstrap-5.2.0-dist
COPY ./Click2Call ./Click2Call
COPY ./Config ./Config

ADD db.sqlite3 .
ADD manage.py .
ADD Pipfile .
ADD Pipfile.lock .

CMD ["python","./manage.py", "runserver"]

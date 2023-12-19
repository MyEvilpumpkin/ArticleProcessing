FROM python:3.9.6-slim

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3"]

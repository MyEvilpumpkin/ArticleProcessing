FROM python:3.9.6-slim

RUN apt update -y && apt install -y gcc python3-dev

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

ENV PYTHONPATH=/app

ENTRYPOINT ["python3"]

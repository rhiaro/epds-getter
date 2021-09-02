FROM python:3.6

WORKDIR /epds

COPY . .
RUN pip install -e .

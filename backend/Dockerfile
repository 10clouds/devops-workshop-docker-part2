# pull official base image
FROM python:3.8.6-slim-buster

# install mysql dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc && \
    apt-get clean -y

# create application user
RUN adduser --disabled-password --gecos '' django
USER django

# set output to unbuffered to help collect logs
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

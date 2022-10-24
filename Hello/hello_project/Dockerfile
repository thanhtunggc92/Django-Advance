# pull base image
FROM python:3.10

# set environmnet variables

ENV PYTHONDONTWEITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#Install dependencies 
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project

COPY . /code/
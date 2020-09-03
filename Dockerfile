FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY requirements*.txt ./
ARG ENV
RUN if [ "$ENV" = "dev" ] ; then pip install -r requirements-dev.txt ; fi
RUN pip install -r requirements.txt
RUN mkdir /code
WORKDIR /code

COPY ./src /code/

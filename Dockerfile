# pull base image
FROM python:3.8-slim-bullseye

# set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /bloc

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD gunicorn bloc_project.wsgi:application --bind 0.0.0.0:$PORT
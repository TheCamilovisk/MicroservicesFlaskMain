FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
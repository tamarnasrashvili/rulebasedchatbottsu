FROM python:3.8

COPY . /app

WORKDIR /app

RUN ["apt", "update"]
RUN ["python", "-m", "pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "--default-timeout=100", "-r", "requirements.txt"]

EXPOSE 4761
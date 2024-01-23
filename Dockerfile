FROM python:3.12
WORKDIR /usr/src/app

COPY ./src ./
RUN pip install -r requirements.txt


ENV PYTHONUNBUFFERED 1

CMD [ "python", "./app.py" ]
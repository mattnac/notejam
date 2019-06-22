FROM python:2.7-alpine

ADD flask /notejam
WORKDIR /notejam
RUN pip install -r requirements.txt

CMD [ "python", "runserver.py" ]

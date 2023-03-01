FROM python:3.8

WORKDIR /app

#ich kann die Dateien so kopieren, dann wird aber fuer jede ein eigener Layer erstellt:
#COPY requirements.txt .
#COPY app-py . 

#besser: eigenen Ordner und alles aus diesem Ordner in aktuelles Work-verzeichnis (/app) kopieren:
COPY src/* .

RUN pip3 install -r requirements.txt

EXPOSE 80

ENV FLASK_RUN_PORT=80
ENV FLASK_APP=app
#CMD flask run --host=0.0.0.0
CMD ["flask", "run", "-h","0.0.0.0"]

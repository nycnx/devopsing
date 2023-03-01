FROM python:3.8

WORKDIR /app

COPY src/*/ .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENV FLASK_RUN_PORT=8080
ENV FLASK_APP=app

CMD ["flask", "run", "-h","0.0.0.0"]

FROM python:3.7-slim

ENV FLASK_APP hello.py
EXPOSE 5000
WORKDIR /flask

COPY flask-req.txt requirements.txt
COPY hello.py .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","hello.py"]

# Run with
# docker run -d -p 5000:5000 test-flask:0.0.1
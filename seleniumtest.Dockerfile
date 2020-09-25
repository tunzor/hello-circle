FROM selenium/standalone-chrome

WORKDIR /test
USER root

RUN apt-get update && apt-get install -y python3-pip

COPY test.py .
COPY sel-req.txt requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3","test.py" ]

# Local run (flask site running on localhost)
# docker run --network="host" sel-test:0.0.1

# Config host url:
# docker run -e HOST_URL="URL:PORT" sel-test:0.0.1
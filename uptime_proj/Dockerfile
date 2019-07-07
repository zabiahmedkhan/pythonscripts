FROM ubuntu:16.04 

WORKDIR /

RUN apt-get update && apt-get install -y python && apt-get install -y python-pip && pip install flask

COPY uptime.py /

EXPOSE 10500

CMD ["./uptime.py"]

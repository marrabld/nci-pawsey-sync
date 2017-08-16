FROM ubuntu:16.10
MAINTAINER Daniel Marrable "daniel.marrable@landgate.wa.gov.au"
RUN apt-get -y update
RUN apt-get -y install python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]
FROM ubuntu:16.10
MAINTAINER Daniel Marrable "d.marrabld@curtin.edu.au"
RUN apt-get -y update
RUN apt-get -y install python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
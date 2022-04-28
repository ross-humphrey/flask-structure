# base image
FROM python:3.9.4-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/services

# add and install requirements
COPY ./requirements.txt /usr/src/services/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh

# add services
COPY . /usr/src/services

# run server
CMD ["/usr/src/entrypoint.sh"]

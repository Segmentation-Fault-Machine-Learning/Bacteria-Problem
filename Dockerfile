FROM continuumio/anaconda:latest

RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN mkdir -p /var/app/src
COPY ./src /var/app/src
WORKDIR /var/app

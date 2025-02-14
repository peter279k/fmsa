FROM python:3.13-slim

WORKDIR /app

COPY . /app/

RUN apt-get update \
    && apt-get install gcc wget openjdk-17-jdk wget unzip procps -y \
    && wget -O hapi-fhir-7.6.0-cli.zip https://github.com/hapifhir/hapi-fhir/releases/download/v7.6.0/hapi-fhir-7.6.0-cli.zip \
    && mkdir hapi-fhir-cli && cd hapi-fhir-cli \
    && unzip ../hapi-fhir-7.6.0-cli.zip \
    && cd .. \
    && rm -f hapi-fhir-cli.cmd hapi-fhir-7.6.0-cli.zip \
    && apt-get purge -y wget unzip \
    && apt-get autoremove -y \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

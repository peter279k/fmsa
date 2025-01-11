FROM python:3.13-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc wget -y \
    && apt-get clean

# Patching fastapi-gateway/core.py
RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip \
    && wget -O /usr/local/lib/python3.10/site-packages/fastapi_gateway/core.py https://raw.githubusercontent.com/dotX12/fastapi-gateway/89edc1c25cb6c7bdf30e280b0c3de2f80e5c06a5/fastapi_gateway/core.py

COPY . /app/

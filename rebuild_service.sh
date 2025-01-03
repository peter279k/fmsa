#!/bin/bash

echo "Rebuild the ${service_name} is started."

docker compose down $service_name
docker compose build $service_name
docker compose up -d $service_name

docker compose down nginx
docker compose up -d nginx

echo "Rebuild the ${service_name} is done."

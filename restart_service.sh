#!/bin/bash

service_name=$1

echo "Restart the ${service_name} is started."

docker compose down $service_name
docker compose up -d $service_name --remove-orphans

docker compose down nginx
docker compose up -d nginx

echo "Restart the ${service_name} is done."

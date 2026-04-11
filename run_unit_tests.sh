#!/bin/bash

service_name=$1
test_dir=$2
option=$3
ip_address=$4

echo "Running $service_name unit tests is started."

docker compose exec $service_name bash -c "pip install -r requirements-dev.txt"
docker compose exec $service_name bash -c "IP_ADDRESS=$ip_address python -m pytest $option $test_dir"

echo "Running $service_name unit tests is done."

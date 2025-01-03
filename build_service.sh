#!/bin/bash

echo "Building the FMSA is started!"

if [[ ! -f .env ]]; then
    echo ".env file is not found. Please refer .env.example and create it."
    exit 1;
fi;

no_cache=$1

COMPOSE_PROJECT_NAME="fmsa" docker compose build $no_cache

echo "Building the FMSA is done!"

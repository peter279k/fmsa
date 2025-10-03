#!/bin/bash

# Define scaling conditions based on metrics (e.g., CPU usage)
SCALE_UP_THRESHOLD=50
SCALE_DOWN_THRESHOLD=20

api_gateway=fmsa_api_gateway
fhir_converter=fmsa_fhir_converter

limit_counter=5
low_counter=1

while :
do
    echo "Automatic Scaling Checker has been started."
    # Get current CPU usage
    CPU_USAGE_LIST=$(docker stats --no-stream --format "{{.CPUPerc}}" $(docker ps --format "{{.Names}}" | grep "$fhir_converter") | awk -F. '{print $1}' | awk '{print $NF}')
    CPU_USAGE=$(echo $CPU_USAGE_LIST | awk '{print $NF}')

    api_gateway_counter=$(docker service inspect --format='{{.Spec.Mode.Replicated.Replicas}}' $api_gateway)
    fhir_converter_counter=$(docker service inspect --format='{{.Spec.Mode.Replicated.Replicas}}' $fhir_converter)

    # Scale up if CPU usage is above the threshold
    if [ "$CPU_USAGE" -gt "$SCALE_UP_THRESHOLD" ]; then
        if [[ $api_gateway_counter < $limit_counter ]]; then
            docker service scale "$api_gateway=$(($api_gateway_counter + 1))"
            echo "$(date): Scaling up $api_gateway due to high CPU usage: $CPU_USAGE%" >> scaling.log
        fi;
        if [[ $fhir_converter_counter < $limit_counter ]]; then
            docker service scale "$fhir_converter=$(($fhir_converter_counter + 1))"
            echo "$(date): Scaling up $fhir_converter due to high CPU usage: $CPU_USAGE%" >> scaling.log
        fi;
    fi;

    # Scale down if CPU usage is below the threshold
#    if [ "$CPU_USAGE" -lt "$SCALE_DOWN_THRESHOLD" ]; then
#        if [[ $api_gateway_counter > $low_counter ]]; then
#            docker service scale "$api_gateway=$(($api_gateway_counter - 1))"
#            echo "$(date): Scaling down $api_gateway due to low CPU usage: $CPU_USAGE%" >> scaling.log
#        fi;
#        if [[ $fhir_converter_counter > $low_counter ]]; then
#            docker service scale "$fhir_converter=$(($fhir_converter_counter - 1))"
#            echo "$(date): Scaling down $fhir_converter due to low CPU usage: $CPU_USAGE%" >> scaling.log
#        fi;
#    fi;

    echo "Automatic Scaling Checker has been done."
    sleep 3
done;

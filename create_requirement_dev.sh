#!/bin/bash


for dirname in $(ls -al | awk '{print $9}')
do
    if [[ $dirname == "." ]]; then
        continue
    elif [[ $dirname == ".." ]]; then
        continue
    elif [[ $dirname == ".git" ]]; then
        continue
    fi;

    if [[ -f "$dirname/requirements.txt" ]]; then
        check_test_dep=$(cat $dirname/requirements.txt | grep pytest -c)
        if [[ $check_test_dep > 0 ]]; then
            echo "pytest==8.3.4" > "$dirname/requirements-dev.txt"
            echo "pytest-dependency==0.6.0" >> "$dirname/requirements-dev.txt"
            echo "$dirname/requirements-dev.txt file is saved."
        fi;
    fi;
done;

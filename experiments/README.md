# Introduction

This experiment is for verifying the microservice has the graceful shutdown feature.

# RQ1 Setup

- Ensuring the `fmsa` microservice architecture is up-and-running successfully.
- Ensuring the `python-venv` is available.
- If the `fmsa-experiments` venv directory is existed, it should be deleted firstly.
- Running the `python3 -m venv fmsa-experiments` command to create the virtual environment for the experiment.
- Running the `source fmsa-experiments/bin/activate` to change the above virtual environment.
- Running the `pip install -r requiremnets-dev.txt` to install required Python packages.
- Running the `docker compose -f docker-compose-exp.yml up -d` to run the ClickHouse database server.
- Running the `python -m pytest -s test_graceful_shutdown_rq1.py` to execute the graceful shutdown RQ1 test.

# RQ2 Setup

- Ensuring the `fmsa` microservice architecture is up-and-running successfully.
- Running the `docker compose -f docker-compose-exp.yml up -d` to run the ClickHouse database server.
- Running the `run_unit_tests.sh fhir_generator app/tests/ltc_tw_2025/test_ltc_tw_2025_circuit_breaker_pattern_rq2.py -s 172.17.0.1`

# RQ3 Setup

- Please refer the []().

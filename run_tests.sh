#!/usr/bin/env bash

set -euo pipefail

# export env
export PYTHONPATH=.
export PYTHON_ENV=test

# erase coverage data
coverage erase

# run tests
pytest --cov-config .coveragerc --cov-append --cov-report html --cov=. tests

# coverage html report
coverage html

# open coverage report
# open coverage/index.html

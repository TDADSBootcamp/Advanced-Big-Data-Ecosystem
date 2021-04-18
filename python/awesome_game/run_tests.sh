#!/bin/bash

BASEDIR=$( dirname "${BASH_SOURCE[0]}" )

pipenv run python -m doctest ${BASEDIR}/generate_outcomes.py
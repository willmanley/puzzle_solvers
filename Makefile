#!/usr/bin/make -f

# Format the code.
format:
	poetry run black thermometer/

check:
	poetry run black thermometer/ --check --diff
	poetry run isort thermometer/ --check --diff

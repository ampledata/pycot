# Makefile for Python Cursor on Target Module.
#
# Source:: https://github.com/OnBeep/pycot
# Author:: Greg Albrecht <oss@undef.net>
# Copyright:: Copyright 2017 Orion Labs, Inc.
# License:: Apache License, Version 2.0
#


.DEFAULT_GOAL := all


all: develop

install_requirements:
	pip install -r requirements.txt

develop: remember
	python setup.py develop

install: remember
	python setup.py install

uninstall:
	pip uninstall -y pycot

reinstall: uninstall install

remember:
	@echo
	@echo "Hello from the Makefile..."
	@echo "Don't forget to run: 'make install_requirements'"
	@echo

clean:
	@rm -rf *.egg* build dist *.py[oc] */*.py[co] cover doctest_pypi.cfg \
		nosetests.xml pylint.log output.xml flake8.log tests.log \
		test-result.xml htmlcov fab.log .coverage

publish:
	python setup.py register sdist upload

nosetests: remember
	python setup.py nosetests

pep8: remember
	flake8 --max-complexity 12 --exit-zero pycot/*.py tests/*.py

flake8: pep8

lint: remember
	pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" \
		-r n pycot/*.py tests/*.py || exit 0

pylint: lint

test: lint pep8 nosetests

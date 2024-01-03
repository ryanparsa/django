
# Simply by being mentioned as a target,
# this tells make to export all variables to child processes by default.
.EXPORT_ALL_VARIABLES:


# python
PYTHON:=python3.12
VIRTUAL_ENV=${CURDIR}/venv
PATH:=$(VIRTUAL_ENV)/bin:$(PATH)


.PHONY: venv
venv:
	rm -rf $(VIRTUAL_ENV) && $(PYTHON) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install --upgrade pip wheel setuptools
	$(VIRTUAL_ENV)/bin/pip install --requirement requirements.txt

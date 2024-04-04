:PHONY: all clean

SHELL := /bin/bash
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all: $(VENV)/bin/activate 
	$(VENV)/bin/uvicorn src.main:app --reload

$(VENV)/bin/activate: requirements.txt 
	python3 -m venv $(VENV) 
	$(PIP) install -r requirements.txt

clean:
	rm -rf__pycache__
	rm -rf $(VENV)
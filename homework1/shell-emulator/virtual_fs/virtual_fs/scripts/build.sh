#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m unittest discover -s tests

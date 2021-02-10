#!/bin/bash

virtualenv -p /usr/bin/python3 env

source env/bin/activate
pip3 install --upgrade pip
python3 --version
pip3 --version


#!/bin/bash

mkdir data
cd data/
touch transaction_data.csv
touch user_data.json
cd ..
python functions/setup_database.py
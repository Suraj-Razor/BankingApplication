#!/bin/bash

mkdir data
cd data/
if [ -f "transaction_data.csv" ] && [ -f "user_data.json" ]; then
    echo "Files exist, skipping creation."
else
    touch transaction_data.csv
    touch user_data.json
    cd ..
    python3 utils/setup_database.py
fi


import csv
import json

with open("./data/user_data.json", "w") as json_file:
    data = {"user_data": []}
    json.dump(data, json_file, indent=4)

with open("./data/transaction_data.csv", "w") as csvheader:
    writer = csv.writer(csvheader)
    writer.writerow(["user_id", "transaction_date", "transaction_type", "transaction_amount"])

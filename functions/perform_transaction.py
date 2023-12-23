from datetime import date
import csv
import json
from pprint import pprint

def record_transaction(data):
  with open("./data/transaction_data.csv", "a", newline="\n") as csvdata:
    writer = csv.writer(csvdata)
    writer.writerow(data)

def update_balance(user_id, deposit):
  with open("./data/user_data.json", "r") as json_file:
    data = json.load(json_file)
  for user in data["user_data"]:
    print(user)
    if user["user_id"] == int(user_id):
      user["balance"] += deposit
      pprint(user)
      with open("./data/user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def deposit(user_id):
  deposit = int(input("How much would you like to deposit?"))
  new_data = [user_id,date.today(),"deposit",deposit]
  record_transaction(new_data)
  update_balance(user_id, deposit)
  print("Thank you, your trasaction has been successful")

def withdraw(user_id):
  pass
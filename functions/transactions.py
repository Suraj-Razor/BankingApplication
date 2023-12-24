from datetime import date
from functions.get_user_data import get_user_data
import csv
import json
from pprint import pprint

def record_transaction(data):
  with open("./data/transaction_data.csv", "a", newline="\n") as csvdata:
    writer = csv.writer(csvdata)
    writer.writerow(data)

def update_balance(user_id, new_balance):
  with open("./data/user_data.json", "r") as json_file:
    data = json.load(json_file)
  for user in data["user_data"]:
    if user["user_id"] == int(user_id):
      user["balance"] = new_balance
      with open("./data/user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def deposit(user_id):
  user_data = get_user_data(user_id)
  balance = user_data[1]['balance']
  deposit = int(input("\nHow much would you like to deposit?"))
  new_data = [user_id,date.today(),"deposit",deposit]
  record_transaction(new_data)
  new_balance = balance + deposit
  update_balance(user_id, new_balance)
  print("Thank you, your transaction has been successful")

def withdraw(user_id):
  user_data = get_user_data(user_id)
  balance = user_data[1]['balance']
  print(f"Account Balance: ${user_data[1]['balance']}")
  if balance >0:
    withdraw_amount = int(input("How much would you like to withdraw today?"))
    if withdraw_amount <= balance:
      new_balance = balance - withdraw_amount
      update_balance(user_id, new_balance)
      new_data = [user_id,date.today(),"withdraw",withdraw_amount]
      record_transaction(new_data)
      print("Thank you, your transaction has been successful")
    else:
      print("Sorry, you don't have sufficent fund")
  else:
    print(f"Sorry your account balance is ${user_data[1]['balance']}, you can't withdraw.")
  
def transfer(user_id):
  transfer_id = input("\nPlease enter the user ID where would you like to transfer funds to: ?")

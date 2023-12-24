import json
from functions.new_user import NewUser
from functions.transactions import deposit, withdraw
from pprint import pprint
import unittest.mock

def test_new_user_creation():
  addinguser_test1 = NewUser(1234567890, "testing First Name", "testing Last Name", "27/12/1991", "Accountant", "1/75 Fullagar Crescent Higgins 2615", "suraj.shrestha@gmail.com", 1234)
  with open("./data/user_data.json", "r") as json_file:
    data = json.load(json_file)
  user1_retrived = {}
  for user in data["user_data"]:
    if user["user_id"] == int(addinguser_test1.user_id):
      user1_retrived = user
      break
  addinguser_test2 = NewUser(123456789, "testing2 First Name", "testing2 Last Name", "22/10/1996", "Nurse", "6 English Street, Essendon", "suraj.shrestha@outlook.com", 7889)
  with open("./data/user_data.json", "r") as json_file:
    data = json.load(json_file)
  user2_retrived = {}
  for user in data["user_data"]:
    if user["user_id"] == int(addinguser_test2.user_id):
      user2_retrived = user
      break

  assert addinguser_test1.first_name == user1_retrived["first_name"]
  assert addinguser_test1.last_name == user1_retrived["last_name"]
  assert addinguser_test2.first_name == user2_retrived["first_name"]
  assert addinguser_test2.last_name == user2_retrived["last_name"]

def test_deposit_function():
    with unittest.mock.patch('builtins.input', return_value="100"):
        deposit(123456789)
    with open("./data/user_data.json", "r") as json_file:
        data = json.load(json_file)
    for user in data["user_data"]:
        if user["user_id"] == 123456789:
            user_balance = user["balance"]
            break
    assert user_balance == 100 

def test_withdraw_function():
    with unittest.mock.patch('builtins.input', return_value="100"):
        withdraw(123456789)
    with open("./data/user_data.json", "r") as json_file:
        data = json.load(json_file)
    for user in data["user_data"]:
        if user["user_id"] == 123456789:
            user_balance = user["balance"]
            break
    assert user_balance == 0
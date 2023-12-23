from functions.new_user import NewUser
from functions.generate_id import generate_id
from functions.get_user_input import get_input
from functions.set_password import set_pin
from functions.authenticate import user_authentication
from functions.perform_transaction import deposit, withdraw
import os.path
import json
from random import randint

def create_new_user():
  data = get_input()
  print("\nThank you for providing the details\nPlease set an access pin code, which you will require to access your account")
  pin = set_pin()
  id  = generate_id("./data/user_data.json")
  print(f"\nThank you, your unique User ID is: {id}")
  user = NewUser(id, data["First Name"], data["Last Name"], data["Date of Birth"], data["Occupation"], data["Address"],data["Email"],pin)
  print("\nThank you, your account has now been secured with the access pin that you have provided")

bank_login = True
bank_services = False

while bank_login:
  print("\nWelcome to PyBank Solutions\n")
  print("Type 1 to login \nOR\nType 2 and we'll get you up and running in no time\n")
  user_input = input("")
  if user_input == "1":
    authentication = user_authentication()
    if authentication[0]:
      user_id = authentication[1]
      user_transaction = input("What would you like to do today?\n Type 1 to Deposit \n Type 2 to Withdraw \n Type 3 to Edit Personal Details \n or Type 4 to Logout")
      if user_transaction == "1":
        deposit(user_id)
      elif user_transaction == 2:
        withdraw(user_id)
  elif user_input == "2":
    create_new_user()
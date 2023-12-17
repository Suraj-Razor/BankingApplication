from functions.new_user import NewUser
from functions.generate_id import generate_id
from functions.get_user_input import get_input
from functions.set_password import set_pin
from functions.authenticate import user_authentication
import os.path
import json
from random import randint

def create_new_user():
  data = get_input()
  print("\nThank you for providing the details\nPlease set an access pin code, which you will require to access your account")
  pin = set_pin()
  id  = generate_id()
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
  if authentication:
    bank_login = False
  # while authenticated:
  #   print("I'm in")
  #   pass

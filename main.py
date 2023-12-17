from functions.new_user import NewUser
from functions.generate_id import generate_id
from functions.get_user_input import get_input
from functions.set_password import set_pin
import os.path
import json
from random import randint


def create_new_user():
  data = get_input()
  print("Thank you for providing the details\n \n Please set an access pin code pin which you will require to access your account")
  pin = set_pin()
  id  = generate_id()
  user = NewUser(id, data["First Name"], data["Last Name"], data["Date of Birth"], data["Occupation"], data["Address"],data["Email"],pin)
  print("Thank you, your account has now been secured with the access pin that you have provided")

create_new_user()
import json
import os

class NewUser():
  def __init__(self, id, first_name, last_name, dob, occupation, full_home_address, email, access_pin):
    self.user_id = id
    self.first_name = first_name
    self.last_name = last_name
    self.dob = dob
    self.occupation = occupation
    self.full_home_address = full_home_address
    self.email = email
    self.access_pin = access_pin
    self.balance = 0
    new_user_data = {
      "user_id": self.user_id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "dob": self.dob,
      "occupation": self.occupation,
      "home_address": self.full_home_address,
      "email": self.email,
      "access_pin": self.access_pin,
      "balance": self.balance
    }

    try:
      with open("./data/user_data.json", "r") as json_file:
        data = json.load(json_file)
        data["user_data"].append(new_user_data)
      with open("./data/user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        
    except:
      with open("./data/user_data.json", "w") as json_file:
        data = {"user_data":[new_user_data]}
        json.dump(data, json_file, indent=4)
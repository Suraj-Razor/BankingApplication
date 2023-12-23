import os.path
import json
from random import randint

def generate_id(file):
  try:
      with open(file, "r") as json_file:
        data = json.load(json_file)
      user_data = data["user_data"]
      list_of_id = []
      for i in range(len(user_data)):
        list_of_id.append(user_data[i]["user_id"])
      return max(list_of_id) + 1
  except:
      return randint(100, 1000)
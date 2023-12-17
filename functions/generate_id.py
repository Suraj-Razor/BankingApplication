import os.path
import json
from random import randint

def generate_id():
  file_path = "./data/user_data.json"
  file_exists = os.path.exists(file_path)
  if file_exists:
    with open(file_path, "r") as json_file:
      data = json.load(json_file)
    user_data = data["user_input"]
    list_of_id = []
    print(len(user_data))
    for i in range(len(user_data)):
      list_of_id.append(user_data[i]["user_id"])
    print(list_of_id)
    return max(list_of_id)+1
  else:
    return randint(100, 1000)
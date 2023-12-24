import json

def get_user_data(user_id):
  
  with open("./data/user_data.json", "r") as json_data:
    data = json.load(json_data)
  for id, user in enumerate(data["user_data"]):
    if str(user_id) == str(user["user_id"]):
      data_index = id
      return [True, data["user_data"][data_index]]
  else:
    return[False]
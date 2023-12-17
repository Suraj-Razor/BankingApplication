import json

def user_authentication():
  with open("./data/user_data.json", "r") as user_data:
    data = json.load(user_data)

  all_user = data["user_input"]

  user_id = input("Please enter your User ID: ")
  
  for user in all_user:
    if str(user["user_id"]) == user_id:
      enter_password =  True
      try_pass = 1
      while enter_password:
        pin = input("Please provide your pin: ")
        if str(user["access_pin"]) == pin:
          print(f"Welcome, {user['first_name']} {user['last_name']}. You have been sucessfully authenticated")
          return True
        elif try_pass <3:
          print("Wrong Password, try again")
          try_pass += 1
        else:
          return print("Sorry, we can't authenticate you this time. Try a few mins later.")
  else:
    print("User not found")
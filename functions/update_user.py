import json
def user_update(user_id):
   with open("./data/user_data.json", "r") as json_data:
    data = json.load(json_data)
    for user in data["user_data"]:
      if str(user_id) == str(user["user_id"]):
        for field in user:
          if field == "user_id" or field == "access_pin" or field =="balance":
            pass
          else:
            edit_field = input(f"\nWould you like to edit {field}: {user[field]}?\nType 'Yes' to edit or press enter to continue: ")
            if edit_field.lower() == "yes":
              print(f"\nYou are trying to edit {field}\nCurrent {field}: {user[field]}")
              new_value = input(f"Enter new {field}: ")
              while len(new_value) <= 0 or new_value.isspace():
                new_value = input(f"Sorry {field} cannot be blank, please enter the new value or enter 'cancel' to skip: ")
              if new_value.lower() == "cancel":
                print(f"{field} Skipped from editing")
              else:
                user[field] = new_value
                print(f"Successfully edited {field} with: {new_value}")
        print("\nYour details have been saved as below:")
        for field in user:
          print(f" {field}: {user[field]}")
      
    with open("./data/user_data.json", "w") as json_data:
      data = json.dump(data, json_data, indent=4)
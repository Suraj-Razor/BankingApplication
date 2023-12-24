from random import randint
from functions.new_user import NewUser
import json

def set_pin():
  pin_set = False
  while not pin_set:
    set_pin = input("Please set a numeric access pin: ")
    reconfirm_pin = input("Re-enter to confirm access pin: ")
    if set_pin != reconfirm_pin or len(reconfirm_pin) < 0 or set_pin.isnumeric() == False:
      print("Sorry the pin you have entered does not match the criteria, try again")
    else:
      pin_set = True
  return reconfirm_pin


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


def get_input():
  f_name = input("\nWhat is your First Name:\n")
  l_name = input("\nWhat is your Last Name:\n")
  dob = input("\nEnter you Date of birth in dd/mm/yyyy:\n")
  occupation = input("\nEnter your occupation:\n")
  address = input("\nEnter your full residential address:\n")
  email = input("\nEnter your Email:\n")
  data = {"First Name": f_name,
          "Last Name":l_name,
          "Date of Birth":dob,
          "Occupation":occupation,
          "Address": address,
          "Email": email}
  all_data_correct = False
  while not all_data_correct:
    all_data_correct = True
    for field in data:
      if len(data[field]) == 0:
        data[field] = input(f"Sorry {field} cannot be blank, please provide a value: ")
        all_data_correct = False
  print("\nThank you for providing the details\nPlease set an access pin code, which you will require to access your account")
  pin = set_pin()
  id = generate_id("./data/user_data.json")
  print(f"\nThank you, your unique User ID is: {id}")
  user = NewUser(id, data["First Name"], data["Last Name"], data["Date of Birth"], data["Occupation"], data["Address"],data["Email"],pin)
  print("\nThank you, your account has now been secured with the access pin that you have provided")
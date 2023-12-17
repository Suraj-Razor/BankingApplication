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
  return data
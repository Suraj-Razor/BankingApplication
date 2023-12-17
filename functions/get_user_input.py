def get_input():
  f_name = input("What is your First Name:\n")
  l_name = input("What is your Last Name:\n")
  dob = input("Enter you Date of birth in dd/mm/yyyy:\n")
  occupation = input("Enter your occupation:\n")
  address = input("Enter your full residential address:\n")
  email = input("Enter your Email:\n")
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
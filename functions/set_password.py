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
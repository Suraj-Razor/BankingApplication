from functions.new_user import NewUser
from functions.new_user_creation import get_input
from functions.user_authentication import user_authentication
from functions.transactions import deposit, withdraw
from functions.new_user_creation import get_input
from functions.get_user_data import get_user_data
from functions.update_user import user_update
from functions.display_report import display_transactions
import json
from random import randint


bank_login = True
bank_services = False

while bank_login:
  print("\nWelcome to PyBank Solutions\n")
  print("Type 1 to login \nOR\nType 2 and we'll get you up and running in no time\n")
  user_input = input("")
  if user_input == "1":
    authentication = user_authentication()
    if authentication[0]:
      authenticated = True
      while authenticated:
        user_id = authentication[1]
        user_data = get_user_data(user_id)
        print(f"\nHi {user_data[1]['first_name']} {user_data[1]['last_name']}")
        print(f"Your Account Balance: ${user_data[1]['balance']}")
        user_transaction = input("\nWhat would you like to do today?\n Type 1 to Deposit \n Type 2 to Withdraw \n Type 3 to Edit Personal Details \n Type 4 to View Transactions \n or Type 5 to Logout\n")
        if user_transaction == "1":
          deposit(user_id)
        elif user_transaction == "2":
          withdraw(user_id)
        elif user_transaction == "3":
          user_update(user_id)
        elif user_transaction == "4":
          user_selection = input("\n Type 1 to View All Transactions \n Type 2 to view All Deposits \n Type 3 to view All Withdrawls \n Or Type 4 to go back to previous menu: ")
          if user_selection == "1":
            display_transactions(int(user_id),"all")
          elif user_selection == "2":
            display_transactions(int(user_id),"deposit")
          elif user_selection == "3":
            display_transactions(int(user_id),"withdraw")
          else:
            ("Going back to previous menu")
        else:
          break
  elif user_input == "2":
    get_input()
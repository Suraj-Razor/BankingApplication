from functions.get_user_data import get_user_data


def user_authentication():
    user_id = input("Please enter your User ID: ")
    user_data = get_user_data(user_id)
    if user_data[0]:
        enter_password = True
        try_pass = 0
        while enter_password:
            pin = input("Please provide your pin: ")
            if str(user_data[1]["access_pin"]) == pin:
                print(f"\nYou have been successfully authenticated")
                return [True, user_id]
            elif try_pass < 2:
                print("Wrong Password, try again")
                try_pass += 1
            else:
                print("Sorry, we can't authenticate you this time. Try a few mins later.")
                return [False]
    else:
        print("User not found")
        return [False]

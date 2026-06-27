# Expected username and password (you can change the value)


correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username  password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")


correct_username_given = username_input == correct_username
correct_password_given = password_input == correct_password
correct_admin_username = username_input == admin_username
correct_admin_password = password_input == admin_password

correct_credentials = correct_username_given and correct_password_given
correct_credentials1 = correct_admin_username and correct_admin_password

if correct_credentials or correct_credentials1:
    print("Access Granted")

else:
    print("Access Denied")

# Expected password (you can change the value)

correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")
correct_password_given = password_input == correct_password

if password_input == correct_password:
    print("Access Granted")

if password_input != correct_password:
    print("Access Denied")
print ("End")



# TODO: Notify user if password is valid
#print("Access Granted", correct_password_given)

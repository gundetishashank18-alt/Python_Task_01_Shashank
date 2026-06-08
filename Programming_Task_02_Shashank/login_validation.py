username = "admin"
password = "password123"

user_input = input("Username: ")
pass_input = input("Password: ")

if user_input == username and pass_input == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
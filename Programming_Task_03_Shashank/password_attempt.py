correct_password = "Shashank@123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts left.")
        else:
            print("Account Locked")
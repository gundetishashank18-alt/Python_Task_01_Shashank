correct_password = "admin123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. {attempts} attempts left")
        else:
            print("Account Locked")
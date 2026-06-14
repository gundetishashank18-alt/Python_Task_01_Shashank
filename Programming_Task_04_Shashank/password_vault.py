
def add_password():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # File lo append cheyyi
    file = open("passwords.txt", "a")
    file.write("Website: " + website + "\n")
    file.write("Username: " + username + "\n")
    file.write("Password: " + password + "\n")
    file.write("--------------------\n")
    file.close()
    
    print("Password saved successfully!")

def show_passwords():
    print("\n----- Saved Records -----")
    try:
        file = open("passwords.txt", "r")
        data = file.read()
        file.close()
        
        if data == "":
            print("No passwords saved yet.")
        else:
            print(data)
    except:
        print("No passwords saved yet.")

# Menu
print("1. Add New Password")
print("2. Show All Passwords")
choice = input("Enter Choice: ")

if choice == "1":
    add_password()
elif choice == "2":
    show_passwords()
else:
    print("Invalid Choice")
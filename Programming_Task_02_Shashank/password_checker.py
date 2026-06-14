password = input("Password: ")

has_number = False
has_upper = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_number and has_upper:
    print("Strong Password")
elif len(password) >= 8 and (has_number or has_upper):
    print("Moderate Password")
else:
    print("Weak Password")
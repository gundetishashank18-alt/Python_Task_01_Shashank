first_name = input("Enter First Name: ").lower()
last_name = input("Enter Last Name: ").lower()
birth_year = input("Enter Birth Year: ")

username1 = first_name + last_name + birth_year
username2 = first_name[0] + "." + last_name + birth_year[-2:]
username3 = last_name + "_" + first_name
username4 = first_name + birth_year
username5 = last_name + first_name[0] + birth_year

print("\nUsername Suggestions:")
print(f"1. {username1}")
print(f"2. {username2}")
print(f"3. {username3}")
print(f"4. {username4}")
print(f"5. {username5}")
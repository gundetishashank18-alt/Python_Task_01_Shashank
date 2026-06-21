import os

FILE_NAME = "students.txt"


def load_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) >= 5:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "branch": data[2],
                        "email": data[3],
                        "score": int(data[4])
                    })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(
                f"{s['id']},{s['name']},{s['branch']},{s['email']},{s['score']}\n"
            )


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    email = input("Enter Email: ")

    students.append({
        "id": student_id,
        "name": name,
        "branch": branch,
        "email": email,
        "score": 0
    })

    save_students(students)
    print("Student Added Successfully.")


def view_students(students):
    if not students:
        print("No Records Found.")
        return

    for s in students:
        print("\n----------------------")
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Branch:", s["branch"])
        print("Email:", s["email"])
        print("Security Score:", s["score"])


def search_student(students):
    key = input("Enter Name or ID: ")

    found = False

    for s in students:
        if s["id"] == key or s["name"].lower() == key.lower():
            print("\nRecord Found")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Branch:", s["branch"])
            print("Email:", s["email"])
            print("Security Score:", s["score"])
            found = True

    if not found:
        print("Record Not Found")


def delete_student(students):
    student_id = input("Enter Student ID to Delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print("Student Deleted Successfully")
            return

    print("Student Not Found")


def security_assessment(students):
    student_id = input("Enter Student ID: ")

    for s in students:

        if s["id"] == student_id:

            score = 0

            mfa = input("Is MFA Enabled? (yes/no): ").lower()
            password_length = int(input("Password Length: "))
            update = input("System Updated? (yes/no): ").lower()
            antivirus = input("Antivirus Installed? (yes/no): ").lower()

            if mfa == "yes":
                score += 30

            if password_length >= 8:
                score += 25

            if update == "yes":
                score += 25

            if antivirus == "yes":
                score += 20

            s["score"] = score
            save_students(students)

            print("\nSecurity Score:", score, "/100")

            if score >= 90:
                print("Status: Excellent")
            elif score >= 70:
                print("Status: Good")
            elif score >= 50:
                print("Status: Moderate")
            else:
                print("Status: Poor")

            return

    print("Student Not Found")


def generate_report(students):

    total_students = len(students)

    if total_students == 0:
        print("No Records Available")
        return

    total_score = 0
    poor_count = 0

    for s in students:
        total_score += s["score"]

        if s["score"] < 50:
            poor_count += 1

    average_score = total_score / total_students

    print("\n========== REPORT ==========")
    print("Total Students:", total_students)
    print("Average Security Score:", average_score)
    print("Students with Poor Security Ratings:", poor_count)


def password_strength_checker():
    password = input("Enter Password: ")

    if len(password) >= 8:
        print("Strong Password")
    else:
        print("Weak Password")


def username_generator():
    name = input("Enter Name: ")
    birth = input("Enter Birth Year: ")

    username = name.replace(" ", "").lower() + birth

    print("Generated Username:", username)


def blacklist_ip_checker():
    blacklist = [
        "192.168.1.10",
        "10.0.0.5",
        "172.16.1.100"
    ]

    ip = input("Enter IP Address: ")

    if ip in blacklist:
        print("Blacklisted IP")
    else:
        print("IP Not Found")


students = load_students()

while True:

    print("\n==========================")
    print("Student Security Manager")
    print("==========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Security Assessment")
    print("6. Generate Report")
    print("7. Password Strength Checker")
    print("8. Username Generator")
    print("9. Blacklist IP Checker")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        security_assessment(students)

    elif choice == "6":
        generate_report(students)

    elif choice == "7":
        password_strength_checker()

    elif choice == "8":
        username_generator()

    elif choice == "9":
        blacklist_ip_checker()

    elif choice == "10":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
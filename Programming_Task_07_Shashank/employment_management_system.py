import csv

class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary


employees = []


def add_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(emp_id, name, department, designation, salary)
    employees.append(employee)

    print("Employee Added Successfully!")


def view_employees():
    if not employees:
        print("No Employee Records Found!")
        return

    print("\n-----------------------------------------------------------------------")
    print(f"{'ID':<10}{'Name':<20}{'Department':<15}{'Designation':<15}{'Salary'}")
    print("-----------------------------------------------------------------------")

    for emp in employees:
        print(f"{emp.emp_id:<10}{emp.name:<20}{emp.department:<15}{emp.designation:<15}{emp.salary}")


def search_employee():
    choice = input("Search by (1-ID / 2-Name): ")

    if choice == "1":
        value = input("Enter Employee ID: ")
        for emp in employees:
            if emp.emp_id == value:
                print(vars(emp))
                return

    elif choice == "2":
        value = input("Enter Employee Name: ")
        for emp in employees:
            if emp.name.lower() == value.lower():
                print(vars(emp))
                return

    print("Employee Not Found")


def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            emp.department = input("Enter New Department: ")
            emp.designation = input("Enter New Designation: ")
            emp.salary = float(input("Enter New Salary: "))
            print("Employee Updated Successfully!")
            return

    print("Employee Not Found")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found")


def salary_statistics():
    if not employees:
        print("No Employee Records!")
        return

    salaries = [emp.salary for emp in employees]

    print("\nSalary Statistics")
    print("-----------------------")
    print("Highest Salary :", max(salaries))
    print("Lowest Salary  :", min(salaries))
    print("Average Salary :", sum(salaries) / len(salaries))
    print("Total Employees:", len(employees))


def export_data():
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Department", "Designation", "Salary"])

        for emp in employees:
            writer.writerow([
                emp.emp_id,
                emp.name,
                emp.department,
                emp.designation,
                emp.salary
            ])

    print("Data Exported Successfully!")

    print("\nReading Data from employees.csv\n")

    with open("employees.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Salary Statistics")
    print("7. Export Data")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        salary_statistics()

    elif choice == "7":
        export_data()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
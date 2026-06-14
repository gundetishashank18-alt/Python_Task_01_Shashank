
name = input("Enter Name: ")
roll_no = input("Enter Roll No: ")
branch = input("Enter Branch: ")
marks = input("Enter Marks: ")

file = open("student_data.txt", "w")
file.write("Name: " + name + "\n")
file.write("Roll No: " + roll_no + "\n")
file.write("Branch: " + branch + "\n")
file.write("Marks: " + marks + "\n")
file.close()

print("Student Record Saved Successfully")

print("Reading File...")
file = open("student_data.txt", "r")
data = file.read()
file.close()
print(data)
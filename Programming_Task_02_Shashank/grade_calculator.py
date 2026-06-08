marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks < 60 and marks >= 0:
    grade = "F"
else:
    grade = "Invalid Marks"
    
print(f"Grade: {grade}")
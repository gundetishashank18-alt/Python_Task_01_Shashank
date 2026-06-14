
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return (total / 500) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

marks = []
print("Enter marks for 5 subjects:")
for i in range(1, 6):
    mark = int(input(f"Subject {i}: "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = get_grade(percentage)

# Display results
print("\n----- Result -----")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
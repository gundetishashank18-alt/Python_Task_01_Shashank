num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print(f"\nAddition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2!= 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division: Cannot divide by zero")
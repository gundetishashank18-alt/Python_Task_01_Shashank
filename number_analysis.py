N = int(input("Enter a number: "))

total = 0
even_count = 0
odd_count = 0

for i in range(1, N + 1):
    total += i
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Sum = {total}")
print(f"Even Numbers = {even_count}")
print(f"Odd Numbers = {odd_count}")
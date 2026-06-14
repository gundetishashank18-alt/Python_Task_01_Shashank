n = int(input("Enter a number N: "))

total_sum = 0
even_count = 0
odd_count = 0

for i in range(1, n + 1):
    total_sum += i
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Sum = {total_sum}")
print(f"Even Numbers = {even_count}")
print(f"Odd Numbers = {odd_count}")
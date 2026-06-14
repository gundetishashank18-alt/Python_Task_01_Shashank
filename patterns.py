n = 5

# Pattern 1: *
print("Pattern 1:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print()

# Pattern 2: *****
print("Pattern 2:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# Pattern 3: 12345
print("Pattern 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
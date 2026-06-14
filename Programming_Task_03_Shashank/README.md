# Programming Task 03 - Loops, Patterns & Basic Automation

**Author:** Gundeti Shashank  
**Language:** Python  
**Date:** June 2026  

## 📌 Objective

The purpose of this task is to strengthen understanding of loops, iteration, problem-solving, and basic automation concepts. This task implements core programming logic using `for` loops, `while` loops, conditionals, and basic string manipulation.

## 📂 Files in This Task

| File Name | Description |
| --- | --- |
| `multiplication_table.py` | Generates multiplication table for a given number up to 10 |
| `number_analysis.py` | Analyzes numbers from 1 to N: sum, even count, odd count |
| `patterns.py` | Prints 3 different patterns using nested loops |
| `password_attempt.py` | Simulates basic authentication with 3 password attempts |
| `username_generator.py` | Generates 5 username suggestions from user details |
| `number_guessing_game.py` | Bonus: Random number guessing game with attempt counter |

## 🧠 Logic Used

### **1. multiplication_table.py**
- Takes integer input from user
- Uses `for` loop with `range(1, 11)` to iterate 10 times
- Prints `num x i = result` format using f-strings

### **2. number_analysis.py**
- Accepts number N as input
- Initializes `total_sum`, `even_count`, `odd_count` to 0
- Loops from 1 to N using `range(1, N+1)`
- Adds each number to sum
- Uses modulo `% 2` to check even/odd and increments counters
- Displays final results

### **3. patterns.py**
- **Pattern 1:** Increasing stars - Outer loop 1 to 5, print `"*"` * i
- **Pattern 2:** Decreasing stars - Outer loop 5 to 1, print `"*"` * i  
- **Pattern 3:** Numbers - Nested loop. Outer loop for rows, inner loop prints numbers 1 to i

### **4. password_attempt.py**
- Stores predefined password in variable
- `for` loop runs max 3 times for attempts
- `if` condition checks input vs correct password
- `break` on success, else shows remaining attempts
- After 3 fails, prints "Account Locked"

### **5. username_generator.py**
- Takes First Name, Last Name, Birth Year as input
- Uses `.lower()` for consistency
- String slicing `[-2:]` to get last 2 digits of year
- String concatenation to create 5 different username formats
- Demonstrates basic string manipulation

### **6. number_guessing_game.py - Bonus**
- Uses `random.randint(1, 50)` to generate secret number
- `while True` infinite loop for continuous guessing
- `attempts` counter increments each guess
- `if-elif-else` to give hints: too low / too high / correct
- `break` when guessed correctly

## ▶️ How to Run

Make sure Python is installed. Run any file using:

```bash
python multiplication_table.py
python number_analysis.py
python patterns.py
python password_attempt.py
python username_generator.py
python number_guessing_game.py
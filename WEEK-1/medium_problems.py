# -----------------------------------------
# Author: Harikant Sharma
# Date: 2025-08-04
# Week 1 Python Challenge – Medium Solutions
# -----------------------------------------

"""
🧠 Problem 1:
Input 3-digit number. Print sum of its digits.
"""
num = 347
digit_sum = num // 100 + (num // 10) % 10 + num % 10
print(f"Sum of digits of {num} is {digit_sum}")


"""
🧠 Problem 2:
Check if a number is a palindrome (e.g., 121 → True).
"""
num = 1221
original = str(num)
is_palindrome = original == original[::-1]
print(f"{num} is a palindrome: {is_palindrome}")


"""
🧠 Problem 3:
Input a year. Check if it’s a leap year.
"""
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")


"""
🧠 Problem 4:
Input a 5-digit number. Count how many even digits it contains.
"""
num = 48362
even_count = sum(1 for d in str(num) if int(d) % 2 == 0)
print(f"Even digits in {num}: {even_count}")


"""
🧠 Problem 5:
Build a simple calculator: input 2 numbers and an operator (+, -, *, /).
"""
a, b, op = 12, 4, '*'
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
else:
    result = "Invalid operator"
print(f"{a} {op} {b} = {result}")


"""
🧠 Problem 6:
Input an integer. Print a triangle pattern with 1 2 3... up to that number of rows.
"""
n = 4
for i in range(1, n + 1):
    print(' '.join(str(j) for j in range(1, i + 1)))


"""
🧠 Problem 7:
Print reverse of a number without using string functions.
"""
num = 1234
reverse = 0
n = num
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print(f"Reverse of {num} is {reverse}")


"""
🧠 Problem 8:
Input a number. Print all its divisors.
"""
num = 36
divisors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Divisors of {num}: {divisors}")


"""
🧠 Problem 9:
Print all prime numbers between 1 and 100.
"""
primes = []
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
print("Prime numbers from 1 to 100:", primes)


"""
🧠 Problem 10:
Count how many digits a number has (e.g., 456 → 3).
"""
num = 129384
digit_count = len(str(num))
print(f"{num} has {digit_count} digits")


"""
🧠 Problem 11:
Print this pattern (n rows):
*
* *
* * *
"""
n = 3
for i in range(1, n + 1):
    print("* " * i)


"""
🧠 Problem 12:
Input number of seconds. Convert to hours:minutes:seconds format.
"""
seconds = 9634
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining = seconds % 60
print(f"{seconds} sec = {hours:02d}:{minutes:02d}:{remaining:02d}")


"""
🧠 Problem 13:
Check if input number is an Armstrong number (e.g., 153).
"""
num = 153
digits = str(num)
power = len(digits)
total = sum(int(d) ** power for d in digits)
is_armstrong = total == num
print(f"{num} is an Armstrong number: {is_armstrong}")


"""
🧠 Problem 14:
Print a right-angled number triangle using nested loops.
"""
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


"""
🧠 Problem 15:
Take a 2-digit number. Reverse it and check if sum of original and reversed number is even.
"""
num = 42
rev = int(str(num)[::-1])
total = num + rev
is_even = total % 2 == 0
print(f"{num} + {rev} = {total} → Even sum? {is_even}")


"""
🧠 Problem 16:
Count total number of characters, digits, and special characters from input string.
"""
text = "H4rik@nt#2025"
chars = sum(1 for c in text if c.isalpha())
digits = sum(1 for c in text if c.isdigit())
special = len(text) - chars - digits
print(f"Text: {text} → Letters: {chars}, Digits: {digits}, Special: {special}")


"""
🧠 Problem 17:
Input two times (hh:mm). Calculate the difference in minutes.
"""
h1, m1 = 10, 45
h2, m2 = 12, 10
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
diff = abs(t2 - t1)
print(f"Time diff = {diff} minutes")


"""
🧠 Problem 18:
Print a pyramid of # with input height.
"""
height = 4
for i in range(1, height + 1):
    print(' ' * (height - i) + '# ' * i)


"""
🧠 Problem 19:
Check whether a number is perfect (i.e., sum of divisors equals number).
"""
num = 28
divisor_sum = sum(i for i in range(1, num) if num % i == 0)
is_perfect = divisor_sum == num
print(f"{num} is a perfect number: {is_perfect}")


"""
🧠 Problem 20:
Sum all odd numbers between 1 and N (input).
"""
n = 15
odd_sum = sum(i for i in range(1, n + 1, 2))
print(f"Sum of odd numbers from 1 to {n}: {odd_sum}")

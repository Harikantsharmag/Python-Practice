# -----------------------------------------
# Author: Harikant Sharma
# Date: 2025-08-03
# Week 1 Python Challenge – Problem #
# -----------------------------------------

"""
🧠 Problem 1:
Take two numbers as input.
Print their sum, difference, product, and integer division.

"""
num1 = 7
num2 = 3

print(f'Sum: {num1 + num1}\nDifference: {num1 - num2}\nProduct: {num1 * num2}\nInterger Division: {int(num1 / num2)}')


"""
🧠 Problem 2:
Input age.
Print "Teenager" if between 13 and 19, else "Not a teenager".

"""

age = 18

if age >= 13 and age <=19:
    print("Teenager")
else:
    print("Not a Teenager")


"""
🧠 Problem 3:
Input a number.
Print whether it is even or odd.

"""

num3 = 5

if(num3 % 2 == 0):
    print("Even")
else:
    print("Odd")


# -----------------------------------------
# Author: Harikant Sharma
# Date: 2025-08-03
# Week 1 Python Challenge – Easy Problems
# -----------------------------------------

"""
🧠 Problem 4:
Convert Celsius to Fahrenheit.
Formula: F = C * 9/5 + 32
"""
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"Fahrenheit: {fahrenheit}")

"""
🧠 Problem 5:
Input 3 numbers. Print the largest.
"""
a, b, c = 12, 7, 19
print("Largest:", max(a, b, c))

"""
🧠 Problem 6:
Check if a character is a vowel.
"""
ch = 'e'
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

"""
🧠 Problem 7:
Print square if number is positive.
"""
num = 6
if num > 0:
    print("Square:", num ** 2)

"""
🧠 Problem 8:
Check if number is divisible by both 3 and 5.
"""
n = 30
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")

"""
🧠 Problem 9:
Print True if either number is 10 or their sum is 10.
"""
x, y = 3, 7
print(x == 10 or y == 10 or (x + y) == 10)

"""
🧠 Problem 10:
Print numbers from 1 to 50 using a while loop.
"""
i = 1
while i <= 50:
    print(i, end=' ')
    i += 1
print()

"""
🧠 Problem 11:
Print numbers from 100 to 1 using a for loop.
"""
for i in range(100, 0, -1):
    print(i, end=' ')
print()

"""
🧠 Problem 12:
Print all even numbers from 1 to 100.
"""
for i in range(2, 101, 2):
    print(i, end=' ')
print()

"""
🧠 Problem 13:
Print first 10 multiples of a number.
"""
num = 4
for i in range(1, 11):
    print(num * i, end=' ')
print()

"""
🧠 Problem 14:
Count how many numbers between 1 and 100 are divisible by 7.
"""
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("Count:", count)

"""
🧠 Problem 15:
Take 3 marks. If all >= 40, print Pass else Fail.
"""
m1, m2, m3 = 75, 65, 40
if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
else:
    print("Fail")

"""
🧠 Problem 16:
Swap two numbers without using a third variable.
"""
x, y = 5, 9
x = x + y
y = x - y
x = x - y
print("x:", x, "y:", y)

"""
🧠 Problem 17:
Print all lowercase letters from a to z.
"""
for i in range(97, 123):
    print(chr(i), end=' ')
print()

"""
🧠 Problem 18:
Check if a given character is a digit.
"""
char = '7'
print("Digit" if char.isdigit() else "Not a digit")

"""
🧠 Problem 19:
Print triangle of * (height 5)
"""
for i in range(1, 6):
    print('*' * i)

"""
🧠 Problem 20:
Print the sum of first n natural numbers.
"""
n = 10
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum:", sum)

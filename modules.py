# ==========================
# IN-BUILT MODULES
# ==========================

import math
import random
import datetime

print("====== IN-BUILT MODULES ======\n")

num = int(input("Enter a number: "))

print("Square Root :", math.sqrt(num))
print("Cube :", math.pow(num, 3))
print("Factorial :", math.factorial(num))
print("Value of PI :", math.pi)

print("Random Number (1-100):", random.randint(1, 100))

today = datetime.datetime.now()

print("Current Date & Time :", today)
print("Current Year :", today.year)

print("\n===============================")


# ==========================
# USER-DEFINED MODULE
# (Functions created by user)
# ==========================

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible."
    return a / b


print("\n====== USER-DEFINED FUNCTIONS ======\n")

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

print("Addition :", addition(n1, n2))
print("Subtraction :", subtraction(n1, n2))
print("Multiplication :", multiplication(n1, n2))
print("Division :", division(n1, n2))
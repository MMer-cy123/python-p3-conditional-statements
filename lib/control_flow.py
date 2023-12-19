#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.lower() == "admin") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
     if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
     elif num % 3 == 0:
        return "Fizz"
     elif num % 5 == 0:
        return "Buzz"
     else:
        return num

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
# Run some test cases
print(admin_login("sudo", "12345"))  # "Access denied"
print(admin_login("admin", "12345"))  # "Access granted"
print(admin_login("ADMIN", "12345"))  # "Access granted"

print(hows_the_weather(33))  # "It's brisk out there!"
print(hows_the_weather(99))  # "It's too dang hot out there!"
print(hows_the_weather(75))  # "It's perfect out there!"

print(fizzbuzz(1))  # 1
print(fizzbuzz(2))  # 2
print(fizzbuzz(3))  # "Fizz"
print(fizzbuzz(4))  # 4
print(fizzbuzz(5))  # "Buzz"
print(fizzbuzz(15))  # "FizzBuzz"

print(calculator("+", 1, 1))  # 2
print(calculator("-", 3, 1))  # 2
print(calculator("*", 3, 2))  # 6
print(calculator("/", 4, 2))  # 2
print(calculator("nope", 4, 2))  # "Invalid operation!"


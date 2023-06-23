def opening():
    print("The following is a computer application designed to handle the addition, subtraction, multiplication or division of any numbers entered.")

def calculation():
    while True:
        try:
            x = float(input("Value 1: "))
            break
        except ValueError:
            print("Please enter a numerical value, using a numerical key.")
    while True:
        try:
            y = float(input("Value 2: "))
            break
        except ValueError:
            print("Please enter a numerical value, using a numerical key.")
    while True:
        try:
            operator = input("Function (eg. +, -, x, /): ")
            break
        except:
            print("Please enter a valid operator.")
    operation(operator, x, y)

def operation(operator, x, y):
    if operator.strip() == "+":
        answer = x + y
        write_to_file(f"{x} + {y} = {answer}")
    elif operator.strip() == "-":
        answer = x - y
        write_to_file(f"{x} + {y} = {answer}")
    elif operator.strip() == "/":
        try:
            answer = x/y
            write_to_file(f"{x} / {y} = {answer}")
        except ZeroDivisionError:
            print("You cannot divide by 0")
    elif operator.strip() == "x" or operator.strip() == "*":
        answer = x * y
        write_to_file(f"{x} + {y} = {answer}")
    
def write_to_file(operation):
    with open(f"{file_name}.txt", "a") as file:
            file.write(operation)
            file.close

while True:
    print("What would you like to do?\n\nUse a calculator, or read all existing equations?\n ")
    user_choice = input("Please type either 'CALCULATOR' or 'EQUATIONS': ")
    if user_choice.strip().lower() == "calculator":
        opening()
        file_name = input("Please enter a file name: ")
        calculation()
    elif user_choice.strip().lower() == "equations" or user_choice.strip().lower() == "equation":
        user_input = input("Please enter the name of the file you'd like to read from: ")
        try:
            with open(f"{user_input}.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
                    break
        except FileNotFoundError:
            print("This file is not found.")
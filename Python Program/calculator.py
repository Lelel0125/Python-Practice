# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == '+':
    total = round(num1 + num2, 3)
    print(total)
elif operator == '-':
    total = round(num1 - num2, 3)
    print(total)
elif operator == '*':
    total = round(num1 * num2, 3)
    print(total)
elif operator == '/':
    total = round(num1 / num2, 3)
    print(total)
else:
    print(f"{operator} is not a valid operator")
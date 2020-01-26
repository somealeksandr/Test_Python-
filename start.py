from Modules.calc import plus, minus, division, multi
from colorama import Fore

# res = plus(2, 2)
# print("Result => ", res)

# res = minus(2, 2)
# print("Result => ", res)

# res = multi()

# res = division(2, 2)
# print("Result => ", res)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# action = int(input("Enter action: + = 1, - = 2, * = 3, / = 4: "))

# def calculate():
#     if action == 1:
#         res = plus(a, b)
#         print("Plus = ", res)
#     elif action == 2:
#         res = minus(a, b)
#         print("Minus = ", res)
#     elif action == 3:
#         res = multi(a, b)
#         print("Multi = ", res)
#     else:
#         res = division(a, b)
#         print("Division = ", res)

# calculate()





first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator [ + - * / ]: ")

if operator == '+':
    res = plus(first_number, second_number)
    print("Plus => ", res)
elif operator == '-':
    res = minus(first_number, second_number)
    print("Minus => ", res)
elif operator == '*':
    res = multi(first_number, second_number)
    print("Multi => ", res)
else:
    res = division(first_number, second_number)
    print("Division => ", res)   
     


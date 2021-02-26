# simple calculator project
# software project (2)
# by Sakib Shahariar Shimanto
# 25/02/2021

def welcome_note():
    print("*-" * 30 + "*  Welcome To MY Calculator  *" + "-*" * 30)
    print("\n\n")


def menu():
    print("Following operations are available in this calculator:")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print()


def user_choice():
    print("Enter 0 to exit.")
    sign = input("Enter +, -, * or / for your operation: ")
    return sign


def addition():
    count = int(input("Enter total number of number for addition:  "))
    print("Enter ", end='')
    print(count, end='')
    print(" numbers")
    summation = 0
    for _ in range(count):
        summation += int(input())
    print("\nSummation : ", end='')
    print(summation, "\n")


def subtraction():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print("\nSubtraction = ", end='')
    print(a - b, '\n')


def multiplication():
    count = int(input("Enter total number of number for multiplication:  "))
    print("Enter ", end='')
    print(count, end='')
    print(" numbers")
    mul = 1
    for _ in range(count) :
        mul *= int(input())
    print("\nMultiplication : ", end='')
    print(mul, "\n")


def division():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print("\nSubtraction = ", end='')
    print(a / b, '\n')


welcome_note()
while True:
    menu()
    choice = user_choice()
    if choice == '+':
        addition()
    elif choice == '-':
        subtraction()
    elif choice == '*':
        multiplication()
    elif choice == '/':
        division()
    elif choice == '0':
        print()
        print("Thank You for using the calculator")
        break
    else:
        print("Invalid choice.")
        print("Try again!!!")
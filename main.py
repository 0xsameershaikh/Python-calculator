import re
from huepy import *


#Functions Declarations


def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

if __name__ == '__main__':
            print(cyan(bold("MENU")))
            print(italic('1.Add'))
            print(italic('2.Subtract'))
            print(italic('3.Divide'))
            print(italic('4.Multiply'))
            print(italic('5.Exit'))

            while True:
                    try:
                        choice = int(input("Choice: "))

                        number1 = int(input("Enter: "))
                        number2 = int(input("Enter: "))

                        if choice == 1:
                            result = add(number1, number2)
                            print(green((f"Result {result}")))
                            continue
                        if choice == 2:
                            result = subtract(number1, number2)
                            print(green((f"Result {result}")))
                            continue
                        if choice == 3:
                            result = divide(number1, number2)
                            print(green((f"Result {result}")))
                            continue
                        if choice == 4:
                            result = multiply(number1, number2)
                            print(green((f"Result {result}")))
                            continue
                        if choice == 5:
                            print(green((f"Exited")))
                            exit()
                            continue
                    except Exception:
                        print(red("ENTER A NUMERIC VALUE"))






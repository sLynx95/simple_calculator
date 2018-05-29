#!/bin/usr/env python3
def take_arguments():
    while True:
        try:
            num1 = input("First number: ")
            num1 = int(num1)
            num2 = input("Second number: ")
            num2 = int(num2)
        except ValueError:
            print('Please enter value for number, no character!')
        else:
            arg = (int(num1), int(num2))
            return arg
            break


def addition(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        div = (num1/num2)
    except ZeroDivisionError:
        print("Don't division by zero!")
        return 'Loser'
    else:
        return div

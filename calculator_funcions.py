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
            if num1 and num2:
                arg = (int(num1), int(num2))
                return arg
                break
            elif num2 == 0:
                arg = (int(num1))
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


def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)


def first_nums(limit):
    fir = [1]
    for x in range(2, limit):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            fir.append(x)
    return fir


def fib(n):
    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)

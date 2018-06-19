#!/bin/usr/env python3
"""Simple calculator"""

import os
import time
from calculator_funcions import take_arguments, addition, substraction, multiplication, division
from calculator_funcions import factorial, first_nums, fib

print('\tSimple calculator\n Please select number of option and next enter two numbers\n'
      'If you want quit anytime from calculator press "q".')

while True:
    print('Options:\n\t[1] + addition\n\t[2] - substraction\n\t[3] * multiplication\n\t'
          '[4] / division\n\t[5] ! factorial\n\t[6]  first numbers\n\t[7]  fibonacci')
    print('For options: 5, 6, 7 in second number pass zero')
    print('To quit press "q"')
    option = input('Select: ')
    if option.lower() == 'q':
        print('Quit')
        break
    os.system('clear')
    if option == '1':
        num1, num2 = take_arguments()
        print('Result: '+str(addition(num1, num2)))
    elif option == '2':
        num1, num2 = take_arguments()
        print('Result: '+str(substraction(num1, num2)))
    elif option == '3':
        num1, num2 = take_arguments()
        print('Result: '+str(multiplication(num1, num2)))
    elif option == '4':
        num1, num2 = take_arguments()
        print('Result: '+str(division(num1, num2)))
    elif option == '5':
        num1 = take_arguments()
        print('Result: ' + str(factorial(num1)))
    elif option == '6':
        num1 = take_arguments()
        print('Result: ' + str(first_nums(num1)))
    elif option == '7':
        num1 = take_arguments()
        print('Result: ' + str(fib(num1)))
    else:
        print('\tWrong option!!!')
    time.sleep(2)

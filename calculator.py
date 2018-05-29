#!/bin/usr/env python3
"""Simple calculator"""

from simple_calculator.calculator_funcions import take_arguments, addition, substraction, multiplication, division

print('\tSimple calculator\n Please select number of option and next enter two numbers\n'
      'If you want quit anytime from calculator press "q".')

while True:
    print('Options:\n\t[1] + addition\n\t[2] - substraction\n\t[3] * multiplication\n\t[4] / division')
    print('To quit press "q"')
    option = input('Select: ')
    if option.lower() == 'q':
        print('Quit')
        break
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
    else:
        print('\tWrong option!!!')

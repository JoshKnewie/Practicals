"""Asks user for 5 numbers and outputs various things based on numbers"""

# numbers = []
# for number in range(1,6):
#     user_number = int(input("What is the {} number?".format(number)))
#     numbers.append(user_number)
#
# print("The first number is {}".format(numbers[0]))
# print("the last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']

user_entry = input("What is your username?")
if user_entry in usernames:
    print("Access granted")
else:
    print("Access denied!")
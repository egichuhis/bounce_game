
import sys


age = input('Enter your age: ')
if not bool(age.rstrip()):
    print('You need to enter a value for your age')
else:
    print(age)
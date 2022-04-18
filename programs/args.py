'''
argv is not Array it is a List. It is available sys Module.

The Argument which are passing at the time of execution are called Command Line
Arguments.

Write a Program to display Command Line Arguments
'''

from sys import argv
print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv)
print("Command Line Arguments one by one:")
for x in argv:
    print(x)
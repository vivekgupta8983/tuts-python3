"""
Write a Program to Find Minimum Number
"""
from tokenize import Number

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

min = a if a < b and a < c else b if b < c else c
print("Minimum Value:", min)

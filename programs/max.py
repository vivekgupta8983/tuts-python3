"""
Write a Program to find a maximum number 
"""

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

max = a if a > b and a > c else b if b > c else c

print("Maximum Value:", max)

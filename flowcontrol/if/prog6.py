'''
Write a program to check whether the given number is in between 1 and 100?
'''

num = int(input("Enter the Number: "))
if num > 1 and num < 100:
    print("Entered Number {0} is in between 100".format(num))
else:
    print("Entered Number {0} is not in between 100".format(num))

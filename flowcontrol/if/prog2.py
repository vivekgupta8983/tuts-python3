'''
Write a program to find biggest of given 3 numbers from the commad prompt
'''

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
n3 = int(input("Enter 3rd Number: "))
if n1 > n2 and n2 > n3:
    print("Biggest Number is: ", n1)
elif n2 > n3:
    print("Biggest Number is: ", n2)
else:
    print("Biggest Number is: ", n3)

'''
Write a program to read 3 float numbers from the keyboard with , seperator and print their sum.
'''
a,b,c= [int(x) for x in input("Enter 3 float numbers :").split()]
print("The Add is :", a+b+c)
print("The Sub is :", a-b-c)
print("The Mul is :", a*b*c)

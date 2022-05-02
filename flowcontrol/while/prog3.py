'''
Write a program to display *'s in pyramid style(also known as equivalent triangle)
'''
n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* "*i)

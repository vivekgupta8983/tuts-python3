'''
Write a program to dispaly *'s in Right angled triangle form
'''
n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# Alternate way

# n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    print("* " * i)

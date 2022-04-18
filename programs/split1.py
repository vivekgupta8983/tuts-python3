'''
to read multiple values from the keyboard in a single line

split() function can take space as seperator by default .But we can pass
anything as seperator.
'''

a,b= [int(x) for x in input("Enter 2 numbers :").split()]
print("Sum :", a+b)
print("Minus :", a-b)
print("Division :", a/b)
print("Multiplication :", a*b)
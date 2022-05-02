from sys import argv
sum = 0
mul = 1
args = argv[1:]
for x in args:
    n = int(x)
    sum = sum+n
    mul = mul*n
print("The Sum:", sum)
print("The Mul:", mul)

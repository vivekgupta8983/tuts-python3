'''
Write a Program to access each Character of String in Forward 
and Backward Direction by using while Loop?
'''
s = "Learning Python is very easy !!!"
n = len(s)
i = 0
print("\nForward Direction\n")
while i < n:
    print(s[i], end='')
    i += 1

print("\nBackward Direction\n")
i = -1
while i >= -n:
    print(s[i], end='')
    i = i-1

# Alternative ways

s = "Learning Python is very easy !!!"
print("\n\nForward direction\n\n")
for i in s:
    print(i, end='')

print("\n\nForward direction\n\n")
for i in s[::]:
    print(i, end='')

print("\n\nBackward direction\n\n")
for i in s[::-1]:
    print(i, end='')

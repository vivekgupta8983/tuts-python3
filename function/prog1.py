'''
Write a function to find factorial of given number?
'''
def fact(num):
    result = 1
    while num >=1:
        result=result*num
        num=num-1
    return result
for i in range(1,10):
    print("The Factorial of ",i, "is : ",fact(i))
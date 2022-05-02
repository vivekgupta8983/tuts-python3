'''
Write a Program to Accept some String from the Keyboard and 
display its Characters by Index wise (both Positive and Negative Index)
'''

s=input("Enter the String: ")
i=0
for x in s:
    print("The character present at +ve index {} and at -ve index {} is {}".format(i,i-len(s),x))
    i=i+1
    
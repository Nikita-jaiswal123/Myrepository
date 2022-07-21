# Write a Python Program to Count the Number of Digits in a Number?

n=int(input("entr a number : "))
c=0
while n:
    n=n//10
    c+=1
print("changes done")
print("count of digits of given number is: ",c)

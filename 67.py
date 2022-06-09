#check krishnamurthy no.
import math

num1=int(input('enter the  number ='))
num2=num1
sum=0

while(num2>0):
    fact=1
    i=1
    rem=num2%10
    fact=math.factorial(rem)
    sum=sum+fact
    num2=num2//10

if sum==num1:
    print("%d is a krishnamurty no."%num1)
else:
    print("%d ia not a krishnamurty no."%num1)


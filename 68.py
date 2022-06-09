#chck neon number
import math
 
num1=int(input("enter any no."))

sum=0
square=pow(num1,2)

while(square>0):
   
    
    rem=square%10
  
    sum=sum+rem
    square=square//10

if sum==num1:
    print("%d is a neon no."%num1)
else:
    print("%d ia not a neonno."%num1)


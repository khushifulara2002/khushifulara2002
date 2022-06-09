#check perferct no.

num=int(input("enter any no.="))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("%d ia a perfect no."%num)
else:
    print("%d ia  not a perfect no."%num)
    

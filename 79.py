#chk strong no

num=int(input("enter any non="))
s=0
temp=num
while(temp>0):
    fact=1
    rem=temp%10
    for i in range(1,rem+1):
        fact=fact*i
    print("factorial of %d = %d"%(rem,fact))
    s=s+fact
    temp=temp//10
print("sum of factorials of the no %d =%d"%(num,s))
if(s==num):
    print("%d is a strong no."%num)
else:
    print("%d is not astrong no."%num)

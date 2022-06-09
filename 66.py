#print 1 to 100 harshad number

for i in range(1,101):
    num1=i
    num2=i
    sum=0 
    while (num2!=0):
        rem=num2%10
        num2=int(num2/10)
        sum=sum+rem
        
    if (num1%sum==0):
        print(i)
           

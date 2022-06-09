#check harshad number
num=int(input("enter the numebr"))
number=num
sum=0
while num:
     sum+=num%10
     num//=10
if number%sum==0:
    print('%d is a harshad  number '%(number))
else:
    print("%d is not a harshad number"%(number))

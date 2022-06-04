#find factorial of number
fact=1

num=int(input("enter any positive number"))

if(num==0):
    print("factorial of 0 = 1")

else:
    while(num>0):
        fact=fact*num
        num=num-1
        
print(fact)
   


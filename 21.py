#find all divisors of an integer

a=int(input("enter the integer="))
print("all divisors of {0} = ".format(a))
for i in range(1,a+1):
    if(a%i==0):
        print(i)

#find prime factors of no.

num=int(input("enter any number="))
print("prime factor of %d ="%num)
for i in range(1,num+1):
    if(num%i==0):
        print(i)
    

#python program to check prime number
#python program to check prime number

num=int(input("enter any no.="))
if num>1:
    for i in range(2,num+1): 
         if(num%i==0):
             print(" not a prime no.")
             break
    else:
        print(" a prime no.")

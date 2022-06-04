#find lcm of 2 number

#lcm*hcf=product of 2 no.
#lcm=product of 2 no./hcf
i=1
num1=int(input("enter 1 no="))
num2=int(input("enter 2 no="))

while(i<=num1 and i<=num2):
    if(num1%i==0 and num2%i==0):
       gdc=i
    i=i+1
lcm=(num1*num2)/gdc
print(lcm)

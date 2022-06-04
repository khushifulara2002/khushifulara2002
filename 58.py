#find gdc of 2 no.
i=1
num1=int(input("enter 1 no="))
num2=int(input("enter 2 no="))

while(i<=num1 and i<=num2):
    if(num1%i==0 and num2%i==0):
       gdc=i
    i=i+1
print("gdc of num1 and num2 =",gdc)

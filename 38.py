#sum and average natural number
sum=0
a=int(input("enter lower limit="))
b=int(input("enter upper limit"))
for i in range(a,b+1):
    sum=sum+i
avg=sum/(b-a)
print("avg =",avg)

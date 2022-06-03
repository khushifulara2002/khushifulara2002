#find average and sum of three numbers

a=3
sum=0
for i in range(1,a+1):
    num=int(input("enter %d number ="%i))
    sum=sum+num
avg=sum/a
print("sum  = ",sum)
print("avg =",avg)

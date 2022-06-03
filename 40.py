#find sum of 10 no. until user enter positive no.


a=10
sum=0
for i in range(1,a+1):
    num=int(input("enter %d number ="%i))
    if(num>0):
        break
    sum=num+sum
print("sum",sum)

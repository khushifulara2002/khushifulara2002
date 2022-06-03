#find sum of even no.

sum =0
a=int(input("enter upper limit ="))

print("the sum of even number between 1 and %d = "%a)
for i in range(1,a+1):
    if(i%2==0):
       sum=sum+i
print(sum)

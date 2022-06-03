#find sum and avg of a natural numbers

sum =0
a=int(input("enter upper limit ="))

print("the sum of natural number between 1 and %d = "%a)
for i in range(1,a+1):
   sum=sum+i
avg=sum/a
print(sum)
print(avg)

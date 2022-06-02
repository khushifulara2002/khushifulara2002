#read 10 number and find their sum and average


sum=0
for i in range(1,11):
    b=int(input(" enter %d number =" %i))
   
    sum=b+sum
    
avg=sum/10
print("sum of 10 no.=",sum)
print("average of 10 no.=",avg)



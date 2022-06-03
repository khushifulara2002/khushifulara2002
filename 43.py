#avg and per of 5 subjects of a student

a=5
sum=0
totalMarks=500
for i in range(1,a+1):
    b=float(input("enter marks of %d subject=" %i))
    sum=sum+b
avg=sum/5
per=(sum/totalMarks)*100
print("average =",avg)
print("percentage=",per)

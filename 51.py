#count number of digit in a number
count=0
a=int(input("enter any digit number"))
while(a>0):
    count=count+1
    a=a//10
print(count)

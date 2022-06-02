#program for multiplication table 

a=int(input("enter any number="))
print("multiplication table of {0}=".format(a))
for i in range (a,a+1):
    for j in range (1,11):
       print("{0} * {1} = {2}".format(i,j,i*j))

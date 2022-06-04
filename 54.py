#find factors of number

num=int(input("enter any number = "))
for i in range(1,num+1):
    if(num%i==0):
        print("factor of {0} = {1}".format(num,i))
    i=1+1

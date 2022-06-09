#check pronic no.
  
num=int(input("enter any no.="))
mul=0
for i in range(1,num):
    if(i*(i+1)==num):
        mul=1
if(mul==1):
    print("%d ia a pronic no."%num)
else:
    print("%d ia  not a pronic no."%num)
    

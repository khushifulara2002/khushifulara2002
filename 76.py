#print spy no.

num=int(input('enter any no.'))
sum=0 
mul=1

while(num>0):
    a=num%10
    sum=sum+a  
    mul=mul*a
    num=num//10

if(sum==mul):
    print(" yes it is aa spy no.")
else:
    print(" sorry , noy a spy no.")

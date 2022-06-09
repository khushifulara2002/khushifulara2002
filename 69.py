#check palindrome no.

num=int(input("enter any no.="))
temp=num
reverse =0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(temp==reverse):
    print("%d ia a palindrome no."%temp)
else:
    print("%d ia  not a palindrome no."%temp)
    



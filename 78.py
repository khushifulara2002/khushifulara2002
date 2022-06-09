#reverse a no.
num= int(input("enter any number="))
reverse=0
while num>0:
    digit=num%10
    reverse=(reverse*10)+digit
    num=num//10
print("reverse = "+str(reverse))

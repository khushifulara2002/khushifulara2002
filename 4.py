#MULTIPLY TWO NUMBERS

a=int(input("enter 1st number="))
b=int(input("enter 2nd number="))
c=a*b
print("MULTIPLICATION OF A AND B =",c)

print('Do you want to multiply more two numbers yes(1)or no(0)?')
ans=int(input('1 or 0 ='))
if(ans==1):
    d=int(input("enter 1st number="))
    e=int(input("enter 2nd number="))
    f=d*e
    print("MULTIPLICATION OF D AND E =",f)
else:
    print("okay")

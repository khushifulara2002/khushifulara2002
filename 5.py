#programs for arithmetic operators

a=int(input('enter 1st number='))
b=int(input('enter 2nd number='))
print('choose arithmetic operators you want to use 1 for + , 2 for -,3 for *,4 for -/,5 for %')
c=int(input('enter number 1-5 ='))
if(c==1):
    print('sum of a and b =',(a+b))

if(c==2):
    print('difference of a and b =',(a-b))

if(c==3):
    print('multiplication of a and b =',(a*b))

if(c==4):
    print('division of a and b =',(a/b))

if(c==5):
    print('modulus of a and b=',(a%b))

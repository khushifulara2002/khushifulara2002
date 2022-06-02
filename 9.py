#largest of three number 

a=int(input('enter 1st no.='))
b=int(input('enter 2nd no.='))
c=int(input('enter 3rd no.='))

if(a>=b and a>=c):
    print("{0} is largest among all".format(a))
if(b>=a and b>=c):
    print("{0} is largest among all".format(b))
else:
    print("{0} is largest among all".format(c))

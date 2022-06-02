#roots of a quadratic equations

import math

a=int(input("enter coefficent of x^2  (a) ="))
b=int(input("enter coefficent of x    (b) ="))
c=int(input("enter constant term      (c) ="))
d=(b*b)-(4*a*c)

if(d==0):
     r1=(-b/(2*a))
     r2=(-b/(2*a))
     print("2 real and equal roots are {0} and {1}".format(r1,r2))


elif(d > 0):
    r1=(-b+ math.sqrt(d)/(2*a))
    r2=(-b- math.sqrt(d)/(2*a))
    print("2 real and distinct roots are {0} and {1}".format(r1,r2))


elif(d < 0):
    r1=math.sqrt(-d)/(2*a)
    r2=math.sqrt(-d)/(2*a)
    print("2 complex roots are {0} and {1}".format(r1,r2))

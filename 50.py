#arithmetic calculations using function

num1=int(input("Enter the 1 number ="))
num2=int(input("Enter the 2 number ="))

def add (x,y):
    c=x+y
    print("add of {0} and {1} = {2}".format(x,y,c))
def sub (x,y):
    d=x-y
    print("sub of {0} and {1} = {2}".format(x,y,d))


def mul (x,y):
    e=x*y
    print("mul of {0} and {1} = {2}".format(x,y,e))


def div  (x,y):
    f=x/y
    print("div of {0} and {1} = {2}".format(x,y,f))


def mod (x,y):
    g=x%y
    print("mod of {0} and {1} = {2}".format(x,y,g))

add(num1,num2)
sub(num1,num2)
mul(num1,num2)
div(num1,num2)
mod(num1,num2)



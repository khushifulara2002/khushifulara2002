#fibonacci series
i=0
a=int(input("enter no. of terms "))
a1=0
a2=1
while(a>i):
    if(i<=1):
        nxt_term=i
    else:
        nxt_term=a1+a2
        a1=a2
        a2=nxt_term
    print(nxt_term)
    i=i+1

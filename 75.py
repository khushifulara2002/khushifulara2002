#print 1 to 100 pronic no.

for i in range(1,101):
    temp=0
    for j in range(0,i+1):
        if j*(j+1)==i:
            temp=1
            break
    if(temp==1):
        print(i)

    

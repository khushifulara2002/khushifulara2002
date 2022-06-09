#print 1 to 100 paindrome no.



for i in range(1,101):
    reverse =0
    temp=i


    while(temp>0):
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10
    if(i==reverse):
       print(i)
   

    



#count vowels and constant

str1=input(" enter the string =")
count_v=0
count_c=0
for j in str1:
    if (j=='a'or j=='e'or j=='i' or j=='o'or j=='u'or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
    
        count_v=count_v+1

    else:
        count_c=count_c+1
print("vowels are =",count_v)
print("constants are =" ,count_c)

#count vowels

str1=input(" enter the string =")
count_v=0

for j in str1:
    if (j=='a'or j=='e'or j=='i' or j=='o'or j=='u'or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
    
        count_v=count_v+1
print("vowels =",count_v)

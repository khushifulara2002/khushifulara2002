#count characters frequency in a string

str1="KhushiFulara"

freq={}
for i in str1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(str(freq))

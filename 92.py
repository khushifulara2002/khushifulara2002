#print ascii value of total characters in  a string

str=input("please enter string = ")

for i in range(len(str)):
    print((str[i],ord(str[i])))

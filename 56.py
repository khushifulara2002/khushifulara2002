#print first number of a digit

num=int(input("enter any digit = "))
first=num

while(first>=10):
    first=first//10
print(first)

#pyhthon program to count digit and special character


str1=input(" enter the string =")
count_d=0
count_s=0
count_c=0

for i in range(len(str1)):
    if(str[i].isdigit()):
        count_d=count_d+1
    elif(str[i].isalpha()):
        count_c=count_c+1
    else:
        count_s=count_s+1
print("digits=",count_d)
print("special character",count_s)

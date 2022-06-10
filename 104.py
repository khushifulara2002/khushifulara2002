#chck string is in palindrome

str1=input('enter the string =')
str2=""
for i in str1:
    str2=i+str2
print("reverse=",str2)
if(str1==str2):
    print("palindrome string")
else:
    print("not a palindrome string")

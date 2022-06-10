#check 2 strings are anagram

str1=input("enter string 1 =")
str2=input("enter string 2 =")
if(sorted(str1)==sorted(str2)):
    print("yes strings are anagram")
else:
    print("not anagram")

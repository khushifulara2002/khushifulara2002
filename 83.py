#python program to check alphabet or not

char=input("please enter any character =")
if((char>='a'and char<='z' or char>='A' and char>='Z')):
    print("%c is a alphabet"%char)
else:
    print("%c is not a alphabet"%char)

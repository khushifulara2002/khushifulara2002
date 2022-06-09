#chk digit is an alphabet , digit , special character

ab=input("please enter any character =")
if((ab>='a'and ab<='z' or ab>='A' and ab>='Z')):
    print("%c is a alphabet"%ab)
elif((ab>='0'and ab<='9')):
    print("%c is a digit"%ab)
else:
    print("%c is a special character"%ab)

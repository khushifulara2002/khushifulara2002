#find student grade

a1=int(input("enter marks of 1st subject="))
a2=int(input("enter marks of 2nd subject="))
a3=int(input("enter marks of 3rd subject="))
a4=int(input("enter marks of 4th subject="))
a5=int(input("enter marks of 5th subject="))
#marks of per subject=100 so total=500
marks=a1+a2+a3+a4+a5
percentage=(marks/500)*100

if(percentage>=80):
    print("grade = A")


elif(percentage>=70 ):
    print("grade = B")


elif(percentage>=60 ):
    print("grade = C")


elif(percentage>=50):
    print("grade = D")


elif(percentage>=30):
    print("grade = E")


else:
    print("grade =F")





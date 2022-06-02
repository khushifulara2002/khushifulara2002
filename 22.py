#find compound interest
import math

principle=float(input("enter the principal amount = "))
rate= float(input("enter the annual interest rate = "))

t=int(input("enter number of years = "))

amount=principle*(pow((1+rate/100),t))
compound=amount-principle
print("compound interest=",compound)

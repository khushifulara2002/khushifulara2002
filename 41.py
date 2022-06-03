#calculate electricity bill

power=float(input("enter the power usage in kWh="))
tot=float(input("toal kwh used since last reading="))
ener=float(input("charge per kwh"))
totalEnergy=tot+ener
fee=float(input("enter fixed monthly fees="))
final_bill=totalEnergy+fee
print(final_bill)




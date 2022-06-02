#program to find profit and loss

cp=int(input("enter the cost price="))
sp=int(input("enter the selling price="))

profit=sp-cp
loss=cp-sp
if(cp>sp):
    print("LOSS = {0}".format(loss))
if(cp<sp):
    print("PROFIT = {0}".format(profit))
if(cp==sp):
    print("no loss no profit")

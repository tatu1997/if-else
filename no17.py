cost_price=int(input("enter cost price"))
selling_price=int(input("enter selling price"))
if cost_price>selling_price:
    print("loss")
elif selling_price>cost_price:
    print("profit")
else:
    print("no profit no loss")

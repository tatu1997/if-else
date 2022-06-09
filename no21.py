unit=int(input("enter nmbr"))
quantity=unit*100
if quantity>=1000:
    discount=quantity*10/100
    total=quantity-discount
    print("total amount",total)
else:
    print("none")
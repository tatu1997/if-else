unit=int(input("enter number"))
if unit<50:
    amount=unit*0.50
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill",total)
elif unit<=100:
    amount=unit*0.75
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill",total)
elif unit<=100:
    amount=unit*1.20
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill",total)
elif unit>=250:
    amount=unit*1.50
    surcharge=amount*20/100
    total=amount+surcharge
    print("electricity bill",total)
else:
    print("none")
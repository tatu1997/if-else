unit=int(input("entr nmbr"))
if unit<=100:
    print("no charge")
elif unit>=100:
    amount=unit*5
    print("total bill",amount)
elif unit>=200:
    amount=unit*10
    print("total bill",amount)
else:
    print("none")
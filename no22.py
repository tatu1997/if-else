year=int(input("enter number"))
salary=int(input("enter nmbr"))
if year>5:
    bonus=salary*5/100
    amount=salary+bonus
    print("net bonus amount",amount)
else:
    print("not net bonus amount")
days=int(input("entr nmbr"))
if days<=5:
    charge=days*2
    print("library charge",charge)
elif days>=6 and days<=10:
    charge=days*3
    print("library charge",charge)
elif days>=10 and days<=15:
    charge=days*4
    print("library charge",charge)
elif days>=15:
    charge=days*5
    print("library charge",charge)
else:
    print("not charge")
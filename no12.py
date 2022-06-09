month=input("enter month")
a=("january""march""may""july""august""october""december")
b=("april""june""september")
c=("february")
if month in(a):
    print("31 day in",month)
elif month in(b):
    print("30 day in",month)
elif month in(c):
    print("28 day in",month)
else:
    print("none")
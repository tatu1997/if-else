amount=int(input("enter number"))
if (amount>5):
    a=amount//200
    b=amount%200
    c=b//1000
    d=b%1000
    e=d//100
    f=d%100
    g=f//10
    print("note of 200=a","note of 1000=c","note of 100=d","note of 10=g",)
else:
    print("not amount")
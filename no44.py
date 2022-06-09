a=int(input("entr nmbr"))
b=int(input("entr nmbr"))
c=int(input("entr nmbr"))
if a>b and a<c or a>c and a<b:
    print("a second largest nmbr")
elif b>a and b<c or b>c and b<a:
    print("b is second largest nmbr")
elif c>a and c<b or c>b and c<a:
    print("c is second largest nmbr")
else:
    print("none")
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a<c or a>c and a<b:
    print("a median of three values")
elif b>a and b<c or b>c and b<a:
    print("b median of three values")
elif c>a and c<b or c>b and c<a:
    print("c median of three values")
else:
    print("none")
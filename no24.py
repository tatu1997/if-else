a=int(input("entr 1st nmbr"))
b=int(input("rntr 2nd nmbr"))
c=int(input("entr 3rd nmbr"))
if a>b and a>c:
    print("it is a oldest")
elif b>a and b>c:
    print("it is b oldest")
elif c>a and c>b:
    print("it is c oldest")
if a<b and a<c:
    print("it is a youngest")
elif b<a and b<c:
    print("it is b youngest")
elif c<a and c<b:
    print("it is c youngest")
else:
    print("none")
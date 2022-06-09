a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a==b and b==c:
    print("equalate")
elif a==b or b==c or a==c:
    print("isoscenles")
else:
    print("scalence")
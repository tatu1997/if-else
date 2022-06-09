a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a+b>c or b+c>a or c+a>b:
    print("triangle is valid")
else:
    print("triangle is not valid")
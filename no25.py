a=int(input("enter classes held"))
b=int(input("enter classes attended"))
percentage=b*100/a
if percentage<=75:
    print("student is not allowed to sit in the exam",percentage)
else:
    print("student is allowed to sit in the exam",percentage)
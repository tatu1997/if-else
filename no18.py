phy=int(input("enter nmbr"))
che=int(input("entr nmbr"))
bio=int(input("enter nmbr"))
math=int(input("enter nmbr"))
com=int(input("enter nmbr"))
total=phy+che+bio+math+com
percentage=total*500/100
if percentage>=90:
    print("grade a")
elif percentage>=80:
    print("grade b")
elif percentage>=70:
    print("grade c")
elif percentage>=60:
    print("grade d")
elif percentage>=40:
    print("grade e")
else:
    print("grade f")